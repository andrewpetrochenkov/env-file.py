#!/usr/bin/env bash
{ set +x; } 2>/dev/null

{ set -x; cd "$(mktemp -d)" || exit; { set +x; } 2>/dev/null; }
( set -x; env-file "VAR" "VALUE" )
( set -x; env-file "VAR" )
( set -x; cat .env )

