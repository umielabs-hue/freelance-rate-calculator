"""Designer Profile Example"""
import sys; sys.path.insert(0, "..")
from models import FreelanceProfile

p = FreelanceProfile(
    desired_monthly_income=3500,
    monthly_business_expenses=400,
    tax_rate=0.25,
    benefits_overhead=0.15,
    weekly_work_hours=40,
    utilization_rate=0.60,
    weeks_per_year=48,
    buffer_multiplier=1.2,
)
s = p.summary()
print("Freelance Designer Rates")
print(f"  Minimum:     ${s['minimum_rate']}/hr")
print(f"  Recommended: ${s['recommended_rate']}/hr")
print(f"  Premium:     ${s['premium_rate']}/hr")
