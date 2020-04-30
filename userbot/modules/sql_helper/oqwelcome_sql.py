from sqlalchemy import BigInteger, Boolean, Column, LargeBinary, Numeric, String, UnicodeText
from userbot.modules.sql_helper import SESSION, BASE


class oqwelcome(BASE):
    __tablename__ = "oqwelcome"
    chat_id = Column(Numeric, primary_key=True)
    should_clean_oqwelcome = Column(Boolean, default=False)
    previous_oqwelcome = Column(BigInteger)
    f_mesg_id = Column(Numeric)

    def __init__(
        self,
        chat_id,
        should_clean_oqwelcome,
        previous_oqwelcome,
        f_mesg_id
    ):
        self.chat_id = chat_id
        self.should_clean_oqwelcome = should_clean_oqwelcome
        self.previous_oqwelcome = previous_oqwelcome
        self.f_mesg_id = f_mesg_id


oqwelcome.__table__.create(checkfirst=True)


def get_current_oqwelcome_settings(chat_id):
    try:
        return SESSION.query(oqwelcome).filter(oqwelcome.chat_id == chat_id).one()
    except:
        return None
    finally:
        SESSION.close()


def add_oqwelcome_setting(
    chat_id,
    should_clean_oqwelcome,
    previous_oqwelcome,
    f_mesg_id
):
    adder = SESSION.query(oqwelcome).get(chat_id)
    if adder:
        adder.should_clean_oqwelcome = should_clean_oqwelcome
        adder.previous_oqwelcome = previous_oqwelcome
        adder.f_mesg_id = f_mesg_id
    else:
        adder = oqwelcome(
            chat_id,
            should_clean_oqwelcome,
            previous_oqwelcome,
            f_mesg_id
        )
    SESSION.add(adder)
    SESSION.commit()


def rm_oqwelcome_setting(chat_id):
    rem = SESSION.query(oqwelcome).get(chat_id)
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def update_previous_oqwelcome(chat_id, previous_oqwelcome):
    row = SESSION.query(rkwelcome).get(chat_id)
    row.previous_oqwelcome = previous_oqwelcome
    # commit the changes to the DB
    SESSION.commit()
