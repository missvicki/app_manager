# Generated by Django 4.1.1 on 2022-10-19 20:05

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Technologies",
            fields=[
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "tech_name",
                    models.CharField(
                        choices=[
                            ("Python", "Python"),
                            ("Java", "Java"),
                            ("JavaScript", "JavaScript"),
                            ("Swift", "Swift"),
                            ("C++", "C++"),
                            ("C#", "C#"),
                            ("R", "R"),
                            ("Golang (Go)", "Golang (Go)"),
                            ("C", "C"),
                            ("PHP", "PHP"),
                            ("Objective-C", "Objective-C"),
                            ("TypeScript", "TypeScript"),
                            ("MATLAB", "MATLAB"),
                            ("Kotlin", "Kotlin"),
                            ("VBA", "VBA"),
                            ("Ruby", "Ruby Rails"),
                            ("Scala", "Scala"),
                            ("Visual Basic", "Visual Basic"),
                            ("Rust", "Rust"),
                            ("Dart", "Dart"),
                            ("Perl", "Perl"),
                            ("Elm", "Elm"),
                            ("Pascal", "Pascal"),
                            ("Elixir", "Elixir"),
                            ("Alice", "Alice"),
                            ("Ada", "Ada"),
                            ("Lua", "Lua"),
                            ("Abap", "Abap"),
                            ("FORTRAN", "FORTRAN"),
                            ("Groovy", "Groovy"),
                            ("Cobol", "Cobol"),
                            ("PowerShell", "PowerShell"),
                            ("SQL", "SQL"),
                            ("Julia", "Julia"),
                            ("Haskell", "Haskell"),
                            ("Delphi", "Delphi"),
                            ("Clojure", "Clojure"),
                            ("LISP", "LISP"),
                            ("Ballerina", "Ballerina"),
                            ("BASIC", "BASIC"),
                            ("Speakeasy", "Speakeasy"),
                            ("Simula", "Simula"),
                            ("Smalltalk", "Smalltalk"),
                            ("Prolog", "Prolog"),
                            ("Erlang", "Erlang"),
                            ("Eiffel", "Eiffel"),
                            ("Rebol", "Rebol"),
                            ("Scratch", "Scratch"),
                        ],
                        default="Python",
                        max_length=50,
                    ),
                ),
            ],
            options={
                "db_table": "technology",
            },
        ),
    ]
