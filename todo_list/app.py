<!doctype html>
<html lang="en">
<head>
    <title>To-Do List</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin-bottom: 10px;
        }
        input[type="text"] {
            padding: 5px;
            font-size: 16px;
        }
        button {
            padding: 5px 10px;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <h1>To Do</h1>
    <ul>
        {% for index, todo in todos %}
            <li>
                <input type="checkbox" {% if todo[2] %}checked{% endif %} onclick="window.location.href='/toggle/{{ todo[0] }}'">
                {{ todo[1] }} - <em>Deadline: {{ todo[3] }}</em>
                <a href="/delete/{{ todo[0] }}" style="margin-left: 10px;">Delete</a>
            </li>
        {% endfor %}
    </ul>
    <form method="POST" action="/add">
        <input type="text" name="new_item" placeholder="New Item" required>
        <input type="text" name="deadline" placeholder="Deadline (YYYY-MM-DD)" required>
        <button type="submit">Add</button>
    </form>
</body>
</html>
