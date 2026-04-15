import firebase_admin
from firebase_admin import db


def push_session_update(session):
    ref = db.reference(f"sessions/{session.id}")

    ref.set({
        "status": session.status,
        "current_question_index": session.current_question_index,
        "started_at": session.started_at.isoformat() if session.started_at else None,
    })


def push_players(session):
    ref = db.reference(f"sessions/{session.id}/players")

    data = {
        str(player.id): {
            "nickname": player.nickname,
            "score": player.score,
        }
        for player in session.players.all()
    }

    ref.set(data)