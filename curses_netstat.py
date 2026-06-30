#!/usr/bin/env python3
import curses
import subprocess
import time


REFRESH_SECONDS = 2


def get_netstat_connections():
    try:
        result = subprocess.run(
            ["netstat", "-tunap"],
            text=True,
            capture_output=True,
            check=False,
        )

        if result.returncode != 0:
            return [result.stderr.strip() or "Failed to run netstat. Try running with sudo."]

        lines = result.stdout.splitlines()
        return lines if lines else ["No connections found."]

    except FileNotFoundError:
        return ["netstat not found. Install net-tools: sudo apt install net-tools"]
    except Exception as exc:
        return [f"Error: {exc}"]


def safe_addnstr(stdscr, y, x, text, width, attr=0):
    try:
        height, screen_width = stdscr.getmaxyx()

        if y < 0 or y >= height or x < 0 or x >= screen_width:
            return

        max_width = max(1, min(width, screen_width - x - 1))
        stdscr.addnstr(y, x, text[:max_width], max_width, attr)

    except curses.error:
        pass


def draw_screen(stdscr, lines, scroll):
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    if height < 3 or width < 20:
        safe_addnstr(stdscr, 0, 0, "Terminal too small.", max(1, width - 1))
        stdscr.refresh()
        return scroll

    title = " Open Connections - netstat | q: quit | ↑/↓: scroll | PgUp/PgDn "
    safe_addnstr(stdscr, 0, 0, title.ljust(width - 1), width - 1, curses.A_REVERSE)

    visible_height = height - 2
    max_scroll = max(0, len(lines) - visible_height)
    scroll = max(0, min(scroll, max_scroll))

    visible_lines = lines[scroll:scroll + visible_height]

    for idx, line in enumerate(visible_lines, start=1):
        if idx >= height - 1:
            break
        safe_addnstr(stdscr, idx, 0, line, width - 1)

    footer = f" Refresh: {REFRESH_SECONDS}s | Lines: {len(lines)} | Scroll: {scroll}/{max_scroll} "
    safe_addnstr(stdscr, height - 1, 0, footer.ljust(width - 1), width - 1, curses.A_REVERSE)

    stdscr.refresh()
    return scroll


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.keypad(True)

    scroll = 0
    lines = []
    last_refresh = 0

    while True:
        now = time.time()

        if now - last_refresh >= REFRESH_SECONDS:
            lines = get_netstat_connections()
            last_refresh = now

        scroll = draw_screen(stdscr, lines, scroll)

        key = stdscr.getch()

        if key in (ord("q"), ord("Q")):
            break
        elif key == curses.KEY_DOWN:
            scroll += 1
        elif key == curses.KEY_UP:
            scroll -= 1
        elif key == curses.KEY_NPAGE:
            scroll += 10
        elif key == curses.KEY_PPAGE:
            scroll -= 10

        time.sleep(0.05)


if __name__ == "__main__":
    curses.wrapper(main)
