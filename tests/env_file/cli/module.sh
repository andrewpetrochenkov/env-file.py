#!/usr/bin/env bash
{ set +x; } 2>/dev/null

{ set -x; cd "$(mktemp -d)" || exit; { set +x; } 2>/dev/null; }
( set -x; python -m env_file "VAR" "VALUE" )
( set -x; python -m env_file "VAR" )
( set -x; cat .env )

