from rest_framework import serializers
from .models import Quiz, Question, AnswerOption


class AnswerOptionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = AnswerOption
        fields = ["id", "text", "is_correct", "order"]
        
        
class QuestionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    options = AnswerOptionSerializer(many=True)

    class Meta:
        model = Question
        fields = [
            "id",
            "text",
            "question_type",
            "order",
            "points",
            "options"
        ]

    def validate(self, data):
        options = data.get("options", [])

        if not options:
            raise serializers.ValidationError("Question must have options")

        correct_count = sum(1 for opt in options if opt.get("is_correct"))

        if correct_count == 0:
            raise serializers.ValidationError("At least one correct answer required")

        if data.get("question_type") == "single" and correct_count > 1:
            raise serializers.ValidationError(
                "Single choice question can have only one correct answer"
            )

        return data
    
    
class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Quiz
        fields = [
            "id",
            "title",
            "description",
            "category",
            "tags",
            "is_published",
            "time_per_question",
            "creator",
            "questions"
        ]

    def create(self, validated_data):
        questions_data = validated_data.pop("questions")

        quiz = Quiz.objects.create(**validated_data)

        for question_data in questions_data:
            options_data = question_data.pop("options")

            question = Question.objects.create(
                quiz=quiz,
                **question_data
            )

            AnswerOption.objects.bulk_create([
                AnswerOption(
                    question=question,
                    **option_data
                )
                for option_data in options_data
            ])

        return quiz
    
    def update(self, instance, validated_data):
        questions_data = validated_data.pop("questions", [])

        # update quiz fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        existing_questions = {q.id: q for q in instance.questions.all()}

        for question_data in questions_data:
            options_data = question_data.pop("options", [])
            question_id = question_data.get("id")

            if question_id and question_id in existing_questions:
                question = existing_questions.pop(question_id)

                for attr, value in question_data.items():
                    setattr(question, attr, value)
                question.save()
            else:
                question = Question.objects.create(
                    quiz=instance,
                    **question_data
                )

            existing_options = {o.id: o for o in question.options.all()}

            for option_data in options_data:
                option_id = option_data.get("id")

                if option_id and option_id in existing_options:
                    option = existing_options.pop(option_id)

                    for attr, value in option_data.items():
                        setattr(option, attr, value)
                    option.save()
                else:
                    AnswerOption.objects.create(
                        question=question,
                        **option_data
                    )

            # delete removed options
            for option in existing_options.values():
                option.delete()

        # delete removed questions
        for question in existing_questions.values():
            question.delete()

        return instance