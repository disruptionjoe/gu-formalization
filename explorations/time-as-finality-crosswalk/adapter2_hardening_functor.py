"""Compatibility entrypoint for the corrected ADAPTER2-01 audit.

The prior implementation incorrectly reported that the profile functor
preserved opposite-polarity forks. The authoritative repair-or-downgrade audit
now lives in ``adapter2_repair_audit.py``. This path remains runnable so old
receipts fail toward the corrected result rather than repeating the withdrawn
claim.
"""

from adapter2_repair_audit import main


if __name__ == "__main__":
    main()
