import rumps
from openapi_client import fetch_openapi_usage_statistics
import cairosvg
import tempfile
from threading import Timer
from AppKit import NSApplication, NSApplicationActivationPolicyAccessory


class MenuBarController(rumps.App):
    def __init__(self):
        super(MenuBarController, self).__init__("OpenAPI Usage")
        self.usage = self.get_usage()
        self.title = f"{self.usage} $"

        # Convert SVG icon to PNG
        svg_data = open("OpenAI_Logo.svg", "rb").read()
        png_data = cairosvg.svg2png(svg_data)
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
            f.write(png_data)
            self.icon = f.name

        self.menu = [
            rumps.MenuItem("Refresh", callback=self.refresh_statistics),
        ]

        self.refresh_timer = Timer(60, self.refresh_statistics)
        self.refresh_timer.start()

    def get_usage(self):
        return fetch_openapi_usage_statistics()

    @rumps.clicked("Refresh")
    def refresh_statistics(self, sender=None):
        self.usage = self.get_usage()
        self.title = f"{self.usage} $"
        self.refresh_timer = Timer(60, self.refresh_statistics)
        self.refresh_timer.start()


if __name__ == "__main__":
    # Hide the dock icon
    app = NSApplication.sharedApplication()
    app.setActivationPolicy_(NSApplicationActivationPolicyAccessory)

    menu_bar_controller = MenuBarController()
    menu_bar_controller.run()
