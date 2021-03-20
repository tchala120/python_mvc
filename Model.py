import pymysql


class Model:
    conn = pymysql.connect('localhost', 'root', 'root', 'exit_exam',
                           8889, '/Applications/MAMP/tmp/mysql/mysql.sock')

    def get_subjects(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT SJID, NAME FROM subjects")
            row = cur.fetchall()
        return row

    def get_students(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT STID, FIRSTNAME, LASTNAME "
                        "from students")
            row = cur.fetchall()
        return row

    def get_scores(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT STID, SJID, SCORE FROM scores")
            row = cur.fetchall()
        return row

    def get_scores_with_join(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(
                "SELECT st.FIRSTNAME, st.LASTNAME, sj.NAME, sc.SCORE FROM students st, scores sc, subjects sj WHERE sc.stid = st.stid and sj.SJID = sc.SJID ORDER BY SCORE DESC")
            row = cur.fetchall()
        return row

    def get_votes(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT VOTE_SUBJECT, VOTE_COUNT FROM votes")
            row = cur.fetchall()
        return row

    def get_vote(self, subject_id):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(
                "SELECT VOTE_SUBJECT, VOTE_COUNT FROM votes WHERE VOTE_SUBJECT = %s", (subject_id))
            row = cur.fetchall()
        return row

    def add_new_vote(self, subject_id):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(
                "INSERT INTO votes(VOTE_SUBJECT, VOTE_COUNT) VALUES (%s, 1)", (subject_id))
            row = cur.fetchall()
        return row

    def update_vote(self, subject_id):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(
                "UPDATE votes SET VOTE_COUNT = VOTE_COUNT + 1 WHERE VOTE_SUBJECT = %s", (subject_id))
            row = cur.fetchall()
        return row

    def get_sum_votes(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(
                "SELECT SUM(VOTE_COUNT) FROM votes")
            row = cur.fetchall()
        return row

    def cal_score(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(
                "SELECT * FROM scores WHERE ")
            row = cur.fetchall()
        return row
