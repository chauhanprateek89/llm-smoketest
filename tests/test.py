import json
import app


def write_todo(path, data):
    (path / "todo.json").write_text(json.dumps(data))


def read_todo(path):
    return json.loads((path / "todo.json").read_text())


def test_load_todo_missing_file_returns_empty(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)

    todos = app.load_todo()

    assert todos == []
    out = capsys.readouterr().out
    assert "Starting with an empty list" in out


def test_save_todo_writes_list(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    app.save_todo(["a", "b"])

    assert read_todo(tmp_path) == ["a", "b"]


def test_load_todo_invalid_format_returns_empty(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    write_todo(tmp_path, {"tasks": []})  # wrong format for this app

    todos = app.load_todo()

    assert todos == []
    out = capsys.readouterr().out
    assert "Invalid todo list format" in out


def test_add_task_adds_new_task(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    write_todo(tmp_path, [])

    app.add_task("buy milk")

    assert read_todo(tmp_path) == ["buy milk"]


def test_add_task_does_not_duplicate(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    write_todo(tmp_path, ["buy milk"])

    app.add_task("buy milk")

    assert read_todo(tmp_path) == ["buy milk"]
    out = capsys.readouterr().out
    assert "Task already exists" in out


def test_mark_done_removes_task(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    write_todo(tmp_path, ["a", "b", "c"])

    app.mark_done("2")

    assert read_todo(tmp_path) == ["a", "c"]
    out = capsys.readouterr().out
    assert "marked as done" in out


def test_mark_done_invalid_index(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    write_todo(tmp_path, ["a"])

    app.mark_done("99")

    assert read_todo(tmp_path) == ["a"]
    out = capsys.readouterr().out
    assert "Invalid task index" in out


def test_mark_done_non_numeric(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    write_todo(tmp_path, ["a"])

    app.mark_done("nope")

    assert read_todo(tmp_path) == ["a"]
    out = capsys.readouterr().out
    assert "Please enter a valid number" in out
