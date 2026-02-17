import json
import app


def write_todo(tmp_path, data):
    (tmp_path / "todo.json").write_text(json.dumps(data))


def read_todo(tmp_path):
    return json.loads((tmp_path / "todo.json").read_text())


def test_load_missing_file_returns_empty(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)

    todos = app.load_todo()

    assert todos == []
    assert "Starting with an empty list" in capsys.readouterr().out


def test_save_writes_list(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    app.save_todo(["a", "b"])

    assert read_todo(tmp_path) == ["a", "b"]


def test_load_invalid_format_returns_empty(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    write_todo(tmp_path, {"tasks": []})  # invalid for THIS app (expects list)

    todos = app.load_todo()

    assert todos == []
    assert "Invalid todo list format" in capsys.readouterr().out


def test_add_task_adds_new_task(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    write_todo(tmp_path, [])

    app.add_task("buy milk")

    assert read_todo(tmp_path) == ["buy milk"]


def test_add_task_prevents_duplicates(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    write_todo(tmp_path, ["buy milk"])

    app.add_task("buy milk")

    assert read_todo(tmp_path) == ["buy milk"]
    assert "Task already exists" in capsys.readouterr().out


def test_mark_done_removes_task(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    write_todo(tmp_path, ["a", "b", "c"])

    app.mark_done("2")

    assert read_todo(tmp_path) == ["a", "c"]
    assert "marked as done" in capsys.readouterr().out


def test_mark_done_invalid_index(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    write_todo(tmp_path, ["a"])

    app.mark_done("99")

    assert read_todo(tmp_path) == ["a"]
    assert "Invalid task index" in capsys.readouterr().out


def test_mark_done_non_numeric(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    write_todo(tmp_path, ["a"])

    app.mark_done("nope")

    assert read_todo(tmp_path) == ["a"]
    assert "Please enter a valid number" in capsys.readouterr().out
