import curses

from devices import DeviceType


class DeviceSelector:
    """
    A class for selecting devices to simulate, supporting both curses-based
    and text-based fallback menus.
    """

    def __init__(self):
        """
        Initializes the list of available devices.
        """
        self.devices = DeviceType.list()

    def curses_menu(self, stdscr):
        """
        Interactive menu using curses.

        Args:
            stdscr: The curses standard screen object.

        Returns:
            str: The selected device.
        """
        current_selection = 0  # Tracks the currently selected option

        while True:
            stdscr.clear()
            stdscr.addstr("Simulate devices:\n", curses.A_BOLD)
            stdscr.addstr("Use UP/DOWN to navigate and ENTER to select.\n\n")

            # Render the menu options
            for idx, device in enumerate(self.devices):
                if idx == current_selection:
                    stdscr.addstr(
                        f"> {device}\n", curses.A_REVERSE
                    )  # Highlight the current selection
                else:
                    stdscr.addstr(f"  {device}\n")

            stdscr.refresh()

            # Handle user input
            key = stdscr.getch()
            if key == curses.KEY_UP and current_selection > 0:
                current_selection -= 1
            elif key == curses.KEY_DOWN and current_selection < len(self.devices) - 1:
                current_selection += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:  # Enter key
                return self.devices[current_selection]  # Return the selected device

    def fallback_menu(self) -> DeviceType:
        """
        Fallback text-based menu for non-interactive environments.

        Returns:
            str: The selected device.
        """
        print("Curses not supported. Falling back to text-based menu.")
        print("\nSimulate devices:")
        for idx, device in enumerate(self.devices, start=1):
            print(f"{idx}) {device}")
        choice = input("Enter the number of your choice: ").strip()
        return self.devices[int(choice) - 1]

    def get_selection(self):
        """
        Displays the device selection menu, falling back to text-based if curses fails.

        Returns:
            str: The selected device.
        """
        try:
            return curses.wrapper(self.curses_menu)
        except curses.error:
            return self.fallback_menu()
