from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.base_model import UUIDModel


class Technologies(UUIDModel):
    class TechnologyAvailable(models.TextChoices):
        Python = "Python", _("Python")
        Java = "Java", _("Java")
        JavaScript = "JavaScript", _("JavaScript")
        Swift = "Swift", _("Swift")
        CPlus = "C++", _("C++")
        CHash = "C#", _("C#")
        R = "R", _("R")
        Golang = "Golang (Go)", _("Golang (Go)")
        C = "C", _("C")
        PHP = "PHP", _("PHP")
        ObjectiveC = "Objective-C", _("Objective-C")
        TypeScript = "TypeScript", _("TypeScript")
        MATLAB = "MATLAB", _("MATLAB")
        Kotlin = "Kotlin", _("Kotlin")
        VBA = "VBA", _("VBA")
        Ruby = "Ruby", _("Ruby Rails")
        Scala = "Scala", _("Scala")
        VisualBasic = "Visual Basic", _("Visual Basic")
        Rust = "Rust", _("Rust")
        Dart = "Dart", _("Dart")
        Perl = "Perl", _("Perl")
        Elm = "Elm", _("Elm")
        Pascal = "Pascal", _("Pascal")
        Elixir = "Elixir", _("Elixir")
        Alice = "Alice", _("Alice")
        Ada = "Ada", _("Ada")
        Lua = "Lua", _("Lua")
        Abap = "Abap", _("Abap")
        FORTRAN = "FORTRAN", _("FORTRAN")
        Groovy = "Groovy", _("Groovy")
        Cobol = "Cobol", _("Cobol")
        PowerShell = "PowerShell", _("PowerShell")
        SQL = "SQL", _("SQL")
        Julia = "Julia", _("Julia")
        Haskell = "Haskell", _("Haskell")
        Delphi = "Delphi", _("Delphi")
        Clojure = "Clojure", _("Clojure")
        LISP = "LISP", _("LISP")
        Ballerina = "Ballerina", _("Ballerina")
        BASIC = "BASIC", _("BASIC")
        Speakeasy = "Speakeasy", _("Speakeasy")
        Simula = "Simula", _("Simula")
        Smalltalk = "Smalltalk", _("Smalltalk")
        Prolog = "Prolog", _("Prolog")
        Erlang = "Erlang", _("Erlang")
        Eiffel = "Eiffel", _("Eiffel")
        Rebol = "Rebol", _("Rebol")
        Scratch = "Scratch", _("Scratch")

    tech_name = models.CharField(
        max_length=50,
        choices=TechnologyAvailable.choices,
        default=TechnologyAvailable.Python,
    )

    class Meta:
        db_table = "technology"
