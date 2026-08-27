# import mysql.connector


# connection = mysql.connector.connect(
#     host = "localhost",
#     username = "root",
#     # database = "monitored_users",
#     password = "@NH3 is soluble in water"
# )


# cursor = connection.cursor()


# cursor.execute("""
#     CREATE DATABASE genshin_impact;
# """)
# connection.commit()


# cursor.execute("""
#     USE  genshin_impact;
# """)
# connection.commit()


# cursor.execute("""
#     CREATE TABLE characters(
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         char_name VARCHAR(40) NOT NULL,
#         rarity INT NOT NULL,
#         vision VARCHAR(30) NOT NULL,
#         weapon VARCHAR(50) NOT NULL,
#         weapon_rarity INT NOT NULL
#     );
# """)
# connection.commit()


# row1 = {
#     "name": "bennet",
#     "rarity": 5,
#     "vision": "pyro",
#     "weapon": "aquila favonia",
#     "weapon_rarity": 5
# }
# cursor.execute("""
#     INSERT INTO characters(
#         char_name,
#         rarity,
#         vision,
#         weapon,
#         weapon_rarity
#     ) VALUES(
#         %s,
#         %s,
#         %s,
#         %s,
#         %s
#     )
# """, (row1["name"],
#     row1["rarity"],
#     row1["vision"],
#     row1["weapon"],
#     row1["weapon_rarity"],
#     )
# )
# connection.commit()


# cursor.close()
# connection.close()























import mysql.connector

def get_client_policy_criteria(client_name):
    client_db_details = {
        "user": None,
        "policy_criteria": None,
        "query_match_count": None
    }
    connection = mysql.connector.connect(
        host = "localhost",
        username = "root",
        database = "monitored_users",
        password = "@NH3 is soluble in water"
    )

    cursor = connection.cursor()

    cursor.execute("""
        SELECT username, policy_criteria
        FROM users
        WHERE username = %s;
    """, (str(client_name), ))
    # query_result = cursor.fetchone()
    query_result = cursor.fetchall()

    # print(f"policy detail: {query_result} | its type: {type(query_result)}")
    print(f"policy details: {query_result} | its type: {type(query_result)}")

    client_db_details["user"] = query_result[0][0]
    # first index -> list index, second index -> tuple index
    # tuple index represents db column number/name
    client_db_details["policy_criteria"] = query_result[0][1]
    client_db_details["query_match_count"] = len(query_result)

    print(f"client_db_details: {client_db_details}")
    return client_db_details

print(f"get_client_policy_criteria('userB'): {get_client_policy_criteria("userB")}")