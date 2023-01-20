from sqlalchemy import util
from sqlalchemy.dialects.postgresql.psycopg import PGDialect_psycopg
from ._psycopg_common import _CockroachDBDialect_common_psycopg
from .ddl_compiler import CockroachDDLCompiler
from .stmt_compiler import CockroachCompiler
from .stmt_compiler import CockroachIdentifierPreparer


class CockroachDBDialect_psycopg(_CockroachDBDialect_common_psycopg, PGDialect_psycopg):
    driver = "psycopg"  # driver name
    preparer = CockroachIdentifierPreparer
    ddl_compiler = CockroachDDLCompiler
    statement_compiler = CockroachCompiler

    supports_statement_cache = True

    @util.memoized_property
    def _psycopg_json(self):
        from psycopg.types import json
        new_json = type('foo', (), {'Json': json.Jsonb, 'Jsonb': json.Jsonb})
        return new_json
