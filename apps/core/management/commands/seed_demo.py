import datetime as dt

from django.core.management.base import BaseCommand

from apps.core.models import SeedInventory

TODAY = dt.date(2026, 11, 6)

DEMO_TAG = "[DEMO]"

ROWS = [
    # (seed_name, variety, category, quantity, unit, location, expiry, days, viability, source)
    ("Rice", "Tubigan 18 / NSIC Rc 222", "grain", 32, "kilograms", "Seed Vault - Cabinet A",
     dt.date(2027, 6, 30), "114-118 days to maturity", "not published",
     "IRRI Rice Today"),
    ("Rice", "Tubigan 4 / NSIC Rc 134", "grain", 8, "kilograms", "Seed Vault - Cabinet A",
     dt.date(2027, 3, 31), "107 days to maturity", "not published",
     "PhilRice via ReliefWeb"),
    ("Rice", "Tubigan 10 / NSIC Rc 152", "grain", 0, "kilograms", "Seed Vault - Cabinet B",
     dt.date(2026, 9, 15), "109 days to maturity", "not published",
     "PhilRice via ReliefWeb"),
    ("Rice", "Tubigan 14 / NSIC Rc 160", "grain", 25, "kilograms", "Seed Vault - Cabinet B",
     dt.date(2027, 11, 30), "107 days to maturity", "not published",
     "PhilRice via ReliefWeb"),
    ("Rice", "Sahod Ulan 1 / NSIC Rc 192", "grain", 18, "kilograms", "Seed Vault - Cabinet A",
     dt.date(2028, 1, 31), "106 days to maturity", "not published",
     "PhilRice via ReliefWeb"),
    ("Rice", "Tubigan 22 / NSIC Rc 240", "grain", 40, "kilograms", "Cold Room - Shelf 1",
     dt.date(2027, 8, 31), "108-115 days to maturity", "not published",
     "PhilRice"),
    ("Rice", "Malagkit 5 / NSIC Rc 21SR", "grain", 12, "kilograms", "Cold Room - Shelf 1",
     dt.date(2027, 5, 31), "122 days to maturity", "not published",
     "PhilRice"),
    ("Rice", "Mestiso 29 / NSIC Rc 244H", "grain", 6, "kilograms", "Cold Room - Shelf 2",
     dt.date(2026, 12, 1), "113 days to maturity", "not published",
     "PhilRice"),
    ("Rice", "Salinas 6 / NSIC Rc 290", "grain", 22, "kilograms", "Cold Room - Shelf 2",
     dt.date(2027, 9, 30), "113 days to maturity", "not published",
     "PhilRice"),
    ("Rice", "Sahod Ulan 14 / NSIC Rc 418", "grain", 15, "kilograms", "Seed Vault - Cabinet B",
     dt.date(2028, 2, 29), "medium-maturing, rainfed lowland", "not published",
     "UPLB UKDR journal"),
    ("Rice", "Sahod Ulan 36 / NSIC Rc 650", "grain", 30, "kilograms", "Seed Vault - Cabinet A",
     dt.date(2027, 4, 30), "not stated on source page", "not published",
     "MMSU news"),
    ("Corn", "DK 8899S", "grain", 20, "kilograms", "FOG Tool Shed - Bin 3",
     dt.date(2027, 2, 28), "not stated on source page", "about 2 years",
     "DA Region 10 hybrid corn field day"),
    ("Corn", "P4124YHR", "grain", 9, "kilograms", "FOG Tool Shed - Bin 3",
     dt.date(2027, 7, 31), "not stated on source page", "about 2 years",
     "DA Region 10 hybrid corn field day"),
    ("Corn", "NK306BGT", "grain", 0, "kilograms", "FOG Tool Shed - Bin 3",
     dt.date(2026, 10, 20), "not stated on source page", "about 2 years",
     "DA Region 10 hybrid corn field day"),

    ("Yardlong Bean (Sitao)", "Maxi Green", "vegetable", 24, "packets", "Seed Vault - Cabinet A",
     dt.date(2027, 7, 31), "50-60 days after sowing", "about 3 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Yardlong Bean (Sitao)", "Montenegro", "vegetable", 14, "packets", "Seed Vault - Cabinet A",
     dt.date(2027, 2, 28), "45-50 days after sowing", "about 3 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Yardlong Bean (Sitao)", "Arayat White", "vegetable", 7, "packets", "Seed Vault - Cabinet B",
     dt.date(2026, 11, 25), "45-50 days after sowing", "about 3 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Yardlong Bean (Sitao)", "Green Ninja", "vegetable", 18, "packets", "Cold Room - Shelf 1",
     dt.date(2028, 3, 31), "50-55 days after sowing", "about 3 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Yardlong Bean (Sitao)", "Mabunga", "vegetable", 3, "packets", "Seed Vault - Cabinet B",
     dt.date(2027, 6, 30), "57 days after sowing", "about 3 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Bitter Gourd (Ampalaya)", "Green Satellite F1", "vegetable", 16, "packets", "Seed Vault - Cabinet A",
     dt.date(2027, 10, 31), "60-65 days after sowing", "about 4 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Bitter Gourd (Ampalaya)", "Mayon F1", "vegetable", 11, "packets", "Cold Room - Shelf 2",
     dt.date(2027, 5, 31), "50-55 days after sowing", "about 4 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Bitter Gourd (Ampalaya)", "Makiling", "vegetable", 20, "packets", "Seed Vault - Cabinet B",
     dt.date(2028, 4, 30), "55-60 days after sowing", "about 4 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Bitter Gourd (Ampalaya)", "Everest Green F1", "vegetable", 0, "packets", "FOG Tool Shed - Bin 3",
     dt.date(2027, 8, 31), "60-65 days after sowing", "about 4 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Squash (Kalabasa)", "Victoria F1", "vegetable", 13, "packets", "Seed Vault - Cabinet A",
     dt.date(2027, 9, 30), "73 days after sowing", "about 4 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Squash (Kalabasa)", "Gloria F1", "vegetable", 5, "packets", "Cold Room - Shelf 1",
     dt.date(2026, 12, 4), "82 days after sowing", "about 4 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Squash (Kalabasa)", "Green Rush F1", "vegetable", 21, "packets", "Seed Vault - Cabinet B",
     dt.date(2027, 12, 31), "50-55 days after sowing", "about 4 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Squash (Kalabasa)", "Batac", "vegetable", 9, "packets", "FOG Tool Shed - Bin 3",
     dt.date(2027, 3, 31), "85 days after sowing", "about 4 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Zucchini", "Zucchini Grey", "vegetable", 17, "packets", "Cold Room - Shelf 2",
     dt.date(2028, 5, 31), "55-60 days after sowing", "about 4 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Tomato", "Victory F1", "vegetable", 26, "packets", "Seed Vault - Cabinet A",
     dt.date(2027, 8, 31), "90 days after sowing", "4-5 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Tomato", "Hope F1", "vegetable", 12, "packets", "Cold Room - Shelf 1",
     dt.date(2027, 4, 30), "80-90 days after sowing", "4-5 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Tomato", "Maunlad", "vegetable", 4, "packets", "Seed Vault - Cabinet B",
     dt.date(2026, 11, 18), "80 days after sowing", "4-5 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Tomato", "Mapalad", "vegetable", 0, "packets", "FOG Tool Shed - Bin 3",
     dt.date(2026, 8, 31), "80 days after sowing", "4-5 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Tomato", "Maguilas", "vegetable", 19, "packets", "Seed Vault - Cabinet A",
     dt.date(2028, 6, 30), "80-85 days after sowing", "4-5 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Eggplant (Talong)", "Champion F1", "vegetable", 23, "packets", "Cold Room - Shelf 2",
     dt.date(2027, 11, 30), "65-68 days after sowing", "about 4 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Eggplant (Talong)", "Checkmate F1", "vegetable", 10, "packets", "Seed Vault - Cabinet B",
     dt.date(2027, 1, 31), "65-68 days after sowing", "about 4 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Hot Pepper (Siling Labuyo)", "Hot Pot 207 F1", "vegetable", 28, "packets", "Seed Vault - Cabinet A",
     dt.date(2027, 7, 31), "100-105 days after sowing", "2-3 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Sweet Pepper", "Green Bell F1", "vegetable", 6, "packets", "Cold Room - Shelf 1",
     dt.date(2026, 12, 5), "55-60 days after sowing", "2-3 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Winged Bean (Sigarilyas)", "Long", "vegetable", 15, "packets", "FOG Tool Shed - Bin 3",
     dt.date(2028, 1, 31), "72 days after sowing", "about 3 years",
     "Kaneko Seeds Philippines catalogue"),

    ("Watermelon", "Sugar Mommy F1", "fruit", 8, "packets", "Seed Vault - Cabinet B",
     dt.date(2027, 6, 30), "60-65 days after sowing", "about 4 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Watermelon", "Sugar Baby", "fruit", 14, "packets", "Cold Room - Shelf 2",
     dt.date(2027, 10, 31), "80-90 days after sowing", "about 4 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Watermelon", "Yellow Baby F1", "fruit", 20, "packets", "Seed Vault - Cabinet A",
     dt.date(2028, 2, 29), "65-70 days after sowing", "about 4 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Watermelon", "Black Tiger F1", "fruit", 0, "packets", "FOG Tool Shed - Bin 3",
     dt.date(2026, 10, 5), "73 days after sowing", "about 4 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Melon", "Sweet Dreams", "fruit", 11, "packets", "Cold Room - Shelf 1",
     dt.date(2027, 5, 31), "70-75 days after sowing", "about 5 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Melon", "Candaba Sweet", "fruit", 17, "packets", "Seed Vault - Cabinet B",
     dt.date(2027, 12, 31), "65-70 days after sowing", "about 5 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Melon", "Honey Dew", "fruit", 30, "packets", "Seed Vault - Cabinet A",
     dt.date(2028, 3, 31), "70-75 days after sowing", "about 5 years",
     "Kaneko Seeds Philippines catalogue"),

    ("Basil", "Prospera Italian Large Leaf DMR (ILL2)", "herb", 9, "packets", "Lab Office - Drawer 2",
     dt.date(2027, 2, 28), "74 days to maturity, 5-10 days to germinate", "not published",
     "Johnny's Selected Seeds"),

    ("Marigold", "Coco Mix", "flower", 450, "grams", "Lab Office - Drawer 2",
     dt.date(2029, 5, 31), "not stated on source page", "3-5 years",
     "Johnny's Selected Seeds"),
    ("Sunflower", "Yellow Queen F1", "flower", 22, "packets", "Seed Vault - Cabinet B",
     dt.date(2028, 8, 31), "not stated on source page", "about 2 years",
     "Kaneko Seeds Philippines catalogue"),
    ("Sunflower", "ProCut Sun Lite Mix", "flower", 16, "packets", "Cold Room - Shelf 2",
     dt.date(2027, 9, 30), "not stated on source page", "about 2 years",
     "Johnny's Selected Seeds"),
    ("Zinnia", "Aurora", "flower", 200, "grams", "Lab Office - Drawer 2",
     dt.date(2029, 6, 30), "not stated on source page", "5 or more years",
     "Johnny's Selected Seeds"),
    ("Cosmos", "Bright Lights", "flower", 19, "packets", "Seed Vault - Cabinet A",
     dt.date(2029, 7, 31), "7-10 days to germinate", "not published",
     "Johnny's Selected Seeds"),

    ("Malunggay (Moringa)", "PKM 1", "other", 400, "grams", "FOG Tool Shed - Bin 3",
     dt.date(2027, 11, 30), "pods from the 4th month after transplant", "not published",
     "TNAU Horticulture"),
    ("Malunggay (Moringa)", "PKM 2", "other", 150, "grams", "FOG Tool Shed - Bin 3",
     dt.date(2028, 6, 30), "not stated on source page", "not published",
     "TNAU Horticulture"),
    ("Roselle (Gumamela)", "", "other", 12, "packets", "Lab Office - Drawer 2",
     dt.date(2027, 4, 30), "60 days after sowing", "not published",
     "Kaneko Seeds Philippines catalogue"),
    ("Amaranth (Alukapapu)", "Green", "other", 8, "packets", "Cold Room - Shelf 1",
     dt.date(2026, 11, 30), "30 days after sowing", "not published",
     "Kaneko Seeds Philippines catalogue"),
    ("Pechay", "", "other", 25, "packets", "Seed Vault - Cabinet B",
     dt.date(2027, 8, 31), "75-85 days after sowing", "not published",
     "Kaneko Seeds Philippines catalogue"),
]


def build_notes(source, days, viability):
    return (
        f"{DEMO_TAG} Variety name from {source}. {days}. "
        f"Seed viability range for this crop: {viability}. "
        "Quantity, unit, storage location and expiration date are test values "
        "for this demo, not supplier records."
    )


class Command(BaseCommand):
    help = "Load sourced demo seed varieties, or remove them again with --purge."

    def add_arguments(self, parser):
        parser.add_argument("--purge", action="store_true",
                            help="Delete only the rows this command inserted.")

    def handle(self, *args, **options):
        if options["purge"]:
            deleted, _ = SeedInventory.objects.filter(notes__startswith=DEMO_TAG).delete()
            self.stdout.write(self.style.SUCCESS(f"Removed {deleted} demo rows."))
            return

        remaining = [row for row in ROWS
                     if not SeedInventory.objects.filter(
                         seed_name=row[0], variety=row[1]).exists()]

        if len(remaining) < len(ROWS):
            self.stdout.write(self.style.WARNING(
                f"Skipped {len(ROWS) - len(remaining)} row(s) already present "
                "(same seed_name + variety)."))

        created = 0
        for (name, variety, category, quantity, unit,
             location, expiry, days, viability, source) in remaining:
            SeedInventory.objects.create(
                seed_name=name,
                variety=variety,
                category=category,
                quantity=quantity,
                unit=unit,
                storage_location=location,
                expiration_date=expiry,
                notes=build_notes(source, days, viability),
            )
            created += 1

        self.stdout.write(self.style.SUCCESS(
            f"Inserted {created} rows. Table now holds "
            f"{SeedInventory.objects.count()} item(s)."))
        self.stdout.write("Undo with:  py -3 manage.py seed_demo --purge")
