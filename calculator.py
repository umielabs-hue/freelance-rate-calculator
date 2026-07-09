"""
Interactive CLI Calculator
Usage: python calculator.py
"""
from models import FreelanceProfile

def ask(prompt, default):
    v = input(f"{prompt} [{default}]: ").strip()
    try: return float(v) if v else float(default)
    except ValueError: return float(default)

def main():
    print("=" * 50)
    print("  FREELANCE RATE CALCULATOR")
    print("=" * 50)
    p = FreelanceProfile(
        desired_monthly_income=ask("Monthly take-home goal ($)", 4000),
        monthly_business_expenses=ask("Monthly business expenses ($)", 500),
        tax_rate=ask("Tax rate (e.g. 0.25)", 0.25),
        benefits_overhead=ask("Benefits overhead (e.g. 0.15)", 0.15),
        weekly_work_hours=ask("Weekly working hours", 40),
        utilization_rate=ask("Utilization rate (e.g. 0.65)", 0.65),
        weeks_per_year=ask("Working weeks/year", 48),
        buffer_multiplier=ask("Buffer multiplier (e.g. 1.2)", 1.2),
    )
    s = p.summary()
    print()
    print("=" * 50)
    print("  YOUR RATES")
    print("=" * 50)
    print(f"  Billable hours/month:  {s['monthly_billable_hours']}h")
    print(f"  Gross needed/month:    ${s['monthly_gross_needed']:,.2f}")
    print()
    print(f"  MINIMUM:               ${s['minimum_rate']:,.2f}/hr")
    print(f"  RECOMMENDED:           ${s['recommended_rate']:,.2f}/hr  <- Use this")
    print(f"  PREMIUM:               ${s['premium_rate']:,.2f}/hr")
    print()
    print(f"  Annual revenue (rec.): ${s['annual_revenue_at_recommended']:,.2f}")
    print("=" * 50)
    print()
    print("TIP: Use RECOMMENDED as your default.")
    print("     Use PREMIUM for urgent/specialized work.")
    print("     Never go below MINIMUM.")

if __name__ == "__main__":
    main()
