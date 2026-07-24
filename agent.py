from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich import box

from tools import crop_tool, irrigation_tool
from image_classifier import predict_disease
from disease import diseases
from chatbot import ask_bot
from weather import get_weather

console = Console()


def show_header():
    console.print(
        Panel.fit(
            "[bold green]🌱 AI CROP ADVISORY SYSTEM[/bold green]\n\n"
            "[cyan]Smart Farming using AI, Machine Learning & Deep Learning[/cyan]",
            border_style="bright_green",
        )
    )


def show_menu():

    table = Table(
        title="[bold bright_blue]MAIN MENU[/bold bright_blue]",
        box=box.ROUNDED,
        border_style="bright_green",
    )

    table.add_column("Option", justify="center", style="cyan", width=10)
    table.add_column("Feature", style="black")

    table.add_row("1", "🌾 Crop Recommendation")
    table.add_row("2", "🍃 Disease Detection")
    table.add_row("3", "💧 Irrigation Recommendation")
    table.add_row("4", "🤖 Agricultural Chatbot")
    table.add_row("5", "🚪 Exit")

    console.print(table)


show_header()

while True:

    show_menu()

    choice = Prompt.ask(
        "[bold purple]Enter your choice[/bold purple]"
    )

    # ===========================================================
    # OPTION 1 : CROP RECOMMENDATION
    # ===========================================================

    if choice == "1":

        console.print()

        console.print(
            Panel.fit(
                "[bold green]🌾 Crop Recommendation[/bold green]",
                border_style="bright_green",
            )
        )

        location = Prompt.ask(
            "[bold purple]Enter City[/bold purple]"
        )

        soil = Prompt.ask(
            "[bold purple]Enter Soil Type[/bold purple]"
        )

        result = crop_tool(location, soil)

        if isinstance(result, str):

            console.print(f"\n[red]{result}[/red]")

        else:

            weather = result["weather"]

            soil_values = result["soil_values"]

            report = Table(
                title="[bold bright_green]🌾 Crop Recommendation Report[/bold bright_green]",
                box=box.DOUBLE_EDGE,
                border_style="bright_green",
            )

            report.add_column("Property",style="bold bright_blue",width=25,justify="left")
            report.add_column("Value",style="bold bright_black",justify="left")

            report.add_row(
                "📍 Location",
                result["location"]
            )

            report.add_row(
                "🌱 Soil Type",
                result["soil"]
            )

            report.add_row(
                "🌡 Temperature",
                f"{weather['temperature']} °C"
            )

            report.add_row(
                "💧 Humidity",
                f"{weather['humidity']} %"
            )

            report.add_row(
                "🌧 Rainfall",
                f"{weather['rainfall']} mm"
            )

            report.add_row(
                "Nitrogen (N)",
                str(soil_values["N"])
            )

            report.add_row(
                "Phosphorus (P)",
                str(soil_values["P"])
            )

            report.add_row(
                "Potassium (K)",
                str(soil_values["K"])
            )

            report.add_row(
                "pH",
                str(soil_values["ph"])
            )

            report.add_row(
                "[bold green]🌾 Recommended Crop[/bold green]",
                f"[bold bright_blue]{result['crop']}[/bold bright_blue]"
            )

            console.print(report)
  
    # ===========================================================
    # OPTION 2 : DISEASE DETECTION
    # ===========================================================

    elif choice == "2":

        console.print()

        console.print(
            Panel.fit(
                "[bold red]🍃 Disease Detection[/bold red]",
                border_style="bright_red",
            )
        )

        image_path = Prompt.ask(
            "[bold purple]Enter Leaf Image Path[/bold purple]"
        )

        try:

            disease_name, confidence = predict_disease(image_path)

            report = Table(
                title="[bold bright_red]🍃 Disease Detection Report[/bold bright_red]",
                box=box.DOUBLE_EDGE,
                border_style="bright_red",
            )

            report.add_column(
                "Property",
                style="bold bright_blue",
                width=22
            )

            report.add_column(
                "Details",
                style="bold bright_black"
            )

            report.add_row(
                "Disease",
                disease_name
            )

            report.add_row(
                "Confidence",
                f"{confidence:.2f}%"
            )

            if disease_name in diseases:

                info = diseases[disease_name]

                report.add_row(
                    "Symptoms",
                    info["Symptoms"]
                )

                report.add_row(
                    "Cause",
                    info["Cause"]
                )

                report.add_row(
                    "Treatment",
                    info["Treatment"]
                )

                report.add_row(
                    "Recommended Fertilizer",
                    info["Fertilizer"]
                )

            else:

                report.add_row(
                    "Information",
                    "No additional information available."
                )

            console.print(report)

        except Exception as e:

            console.print(
                f"[bold red]❌ Error : {e}[/bold red]"
            )


    # ===========================================================
    # OPTION 3 : IRRIGATION RECOMMENDATION
    # ===========================================================

    elif choice == "3":

        console.print()

        console.print(
            Panel.fit(
                "[bold blue]💧 Irrigation Recommendation[/bold blue]",
                border_style="bright_blue",
            )
        )

        city = Prompt.ask(
            "[bold purple]Enter City[/bold purple]"
        )

        weather = get_weather(city)

        if weather is None:

            console.print(
                "[bold red]❌ Unable to fetch weather for the given city.[/bold red]"
            )

        else:

            temp = weather["temperature"]

            humidity = weather["humidity"]

            rainfall = weather["rainfall"]

            recommendation = irrigation_tool(
                temp,
                humidity,
                rainfall
            )

            report = Table(
                title="[bold bright_blue]💧 Irrigation Recommendation[/bold bright_blue]",
                box=box.DOUBLE_EDGE,
                border_style="bright_blue",
            )

            report.add_column(
                "Property",
                style="bold bright_blue",
                width=25
            )

            report.add_column(
                "Value",
                style="bold bright_black"

            )

            report.add_row(
                "📍 Location",
                city.title()
            )

            report.add_row(
                "🌡 Temperature",
                f"{temp} °C"
            )

            report.add_row(
                "💧 Humidity",
                f"{humidity} %"
            )

            report.add_row(
                "🌧 Rainfall",
                f"{rainfall} mm"
            )

            report.add_row(
                "[bold blue]Recommendation[/bold blue]",
                recommendation
            )

            console.print(report)
    # ===========================================================
    # OPTION 4 : AGRICULTURAL CHATBOT
    # ===========================================================

    elif choice == "4":

        console.print()

        console.print(
            Panel.fit(
                "[bold bright_magenta]🤖 Agricultural AI Assistant[/bold bright_magenta]\n"
                "[purple]Ask me anything about crops, diseases, fertilizers, irrigation or farming.[/purple]",
                border_style="bright_magenta",
            )
        )

        question = Prompt.ask(
            "\n[bold bright_green]👨‍🌾 Farmer[/bold bright_green]"
        )

        with console.status(
            "[bold bright_green]🤖 Thinking...[/bold bright_green]"
        ):
            answer = ask_bot(question)

        console.print()

        console.print(
            Panel(
                answer,
                title="[bold bright_green]🌾 AI Assistant[/bold bright_green]",
                border_style="bright_green",
                expand=False,
            )
        )

        console.print(
            "\n[bold bright_yellow]Returning to Main Menu...[/bold bright_yellow]\n"
        )

    # ===========================================================
    # OPTION 5 : EXIT
    # ===========================================================

    elif choice == "5":

        console.print()

        console.print(
            Panel.fit(
                "[bold bright_green]🙏 Thank You for Using[/bold bright_green]\n\n"
                "[bold bright_yellow]🌱 AI Crop Advisory System[/bold bright_yellow]\n\n"
                "[bold bright_cyan]Happy Farming! 🚜🌾[/bold bright_cyan]",
                border_style="bright_green",
            )
        )

        break

    # ===========================================================
    # INVALID CHOICE
    # ===========================================================

    else:

        console.print(
            Panel.fit(
                "[bold bright_red]❌ Invalid Choice[/bold bright_red]\n\n"
                "[bright_white]Please select a valid option from the menu.[/bright_white]",
                border_style="bright_red",
            )
        )

