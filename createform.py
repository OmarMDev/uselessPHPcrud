if 'create' in form:
    name = form.getvalue('name')
    email = form.getvalue('email')
    phone = form.getvalue('phone')
    print(f"Creating user: name={name}, email={email}, phone={phone}")
    cursor.execute("INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
    conn.commit()
    print("User created successfully!")
