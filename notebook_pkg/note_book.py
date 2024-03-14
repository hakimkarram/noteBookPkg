import datetime

last_id = 0


class Note:
    """
    This class uses to create note objects.
    Note object is used to store the memo and tag for searching.
    Attributes:
        - last_id: uses to tracking last note which is registered.
        - ID : to identify the note itself.
        - Memo: which is the test that need to store.
        - Tag: which is the keyword used for searching.
    Actions:
        - match: this method take a search word and ensure if it
                with memo or tag. This method return boolean primitive type.
    """

    def __init__(self, memo, tag=''):
        self.memo = memo
        self.tag = tag
        self.created_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filterWord):
        return filterWord in self.memo or filterWord in self.tag


class NoteBook:
    """
    NoteBook: this class uses to create notebook objects.
              It uses for storing more than one notes and can
              search with it about specific note.
    Attributes:
        - List of notes
    Actions:
        - search(str: string): [] Notes: which accepts string word and to be used for searching inside list of notes.
        - new_note(memo:string, tag:string): It used to create new note and add it to the notes list.
        - modify_memo(note_id, memo): uses to get note by it id and modify its memo with new one.
        - modify_tag(note_id,tag): uses to get note by its id and replace old tag with new tag.
    """

    def __init__(self):
        self.notes = []

    def _find_note(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def search(self, flt):
        return [note for note in self.notes if note.match(flt)]

    def new_note(self, memo, tag):
        self.notes.append(Note(memo, tag))

    def modify_memo(self, note_id, new_memo):
        self._find_note(note_id).memo = new_memo

    def modify_tag(self, note_id, new_tag):
        self._find_note(note_id).tag = new_tag
