def check_readiness(mo):
    with open(".code") as f:
        _s = f.read().strip()
    _msg = ''.join(chr(int(_s[i:i+2], 16) ^ ord("Pontypandy"[(i//2) % 10])) for i in range(0, len(_s), 2))
    return mo.md(f"**{_msg}**")
