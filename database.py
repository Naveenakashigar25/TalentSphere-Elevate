import sqlite3

# Create connection
conn = sqlite3.connect("talentsphere.db", check_same_thread=False)
cursor = conn.cursor()

# Create Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    email TEXT,
    password TEXT,
    category TEXT
)
""")

conn.commit()


# -----------------------------
# Register User
# -----------------------------
def register_user(username, email, password):

    try:
        cursor.execute(
            """
            INSERT INTO users(username,email,password)
            VALUES(?,?,?)
            """,
            (username, email, password)
        )

        conn.commit()
        return True

    except:
        return False


# -----------------------------
# Login User
# -----------------------------
def login_user(username, password):

    cursor.execute(
        """
        SELECT * FROM users
        WHERE username=? AND password=?
        """,
        (username, password)
    )

    return cursor.fetchone()


# -----------------------------
# Save User Category
# -----------------------------
def update_category(username, category):

    cursor.execute(
        """
        UPDATE users
        SET category=?
        WHERE username=?
        """,
        (category, username)
    )

    conn.commit()


# -----------------------------
# View All Users
# -----------------------------
def get_users():

    cursor.execute(
        """
        SELECT id,username,email,category
        FROM users
        ORDER BY id
        """
    )

    return cursor.fetchall()


# -----------------------------
# Total Users
# -----------------------------
def total_users():

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM users
        """
    )

    return cursor.fetchone()[0]


# -----------------------------
# High School Count
# -----------------------------
def highschool_users():

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM users
        WHERE category='High School Student'
        """
    )

    return cursor.fetchone()[0]


# -----------------------------
# Graduate Count
# -----------------------------
def graduate_users():

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM users
        WHERE category='Graduate'
        """
    )

    return cursor.fetchone()[0]


# -----------------------------
# Professional Count
# -----------------------------
def professional_users():

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM users
        WHERE category='Professional'
        """
    )

    return cursor.fetchone()[0]


# -----------------------------
# Delete User
# -----------------------------
def delete_user(username):

    cursor.execute(
        """
        DELETE FROM users
        WHERE username=?
        """,
        (username,)
    )

    conn.commit()


# -----------------------------
# Search User
# -----------------------------
def search_user(username):

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username LIKE ?
        """,
        ("%" + username + "%",)
    )

    return cursor.fetchall()