from sqlalchemy import util
from sqlalchemy.dialects.postgresql.psycopg import (
    PGDialect_psycopg,
    PGDialectAsync_psycopg,
)
from .base import CockroachDBDialect
from .ddl_compiler import CockroachDDLCompiler
from .stmt_compiler import CockroachIdentifierPreparer


class CockroachDBDialectAsync_psycopg(PGDialectAsync_psycopg, CockroachDBDialect):
    driver = "psycopg"  # driver name
    preparer = CockroachIdentifierPreparer
    ddl_compiler = CockroachDDLCompiler

    supports_statement_cache = True

    @util.memoized_property
    def _psycopg_json(self):
        from psycopg.types import json

        new_json = type("foo", (), {"Json": json.Jsonb, "Jsonb": json.Jsonb})
        return new_json


class CockroachDBDialect_psycopg(PGDialect_psycopg, CockroachDBDialect):
    driver = "psycopg"  # driver name
    preparer = CockroachIdentifierPreparer
    ddl_compiler = CockroachDDLCompiler

    supports_statement_cache = True

    @util.memoized_property
    def _psycopg_json(self):
        from psycopg.types import json

        new_json = type("foo", (), {"Json": json.Jsonb, "Jsonb": json.Jsonb})
        return new_json

    @classmethod
    def get_async_dialect_cls(cls, url):
        return CockroachDBDialectAsync_psycopg
