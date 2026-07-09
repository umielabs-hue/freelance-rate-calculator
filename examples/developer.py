"""Developer Profile Example"""
import sys; sys.path.insert(0, "..")
from models import FreelanceProfile

p = FreelanceProfile(
    desired_monthly_income=6000,
    monthly_business_expenses=800,
    tax_rate=0.28,
    benefits_overhead=0.15,
    weekly_work_hours=40,
    utilization_rate=0.70,
    weeks_per_year=48,
    buffer_multiplier=1.25,
)
s = p.summary()
print("Senior Full-Stack Developer Rates")
print(f"  Minimum:     ${s['minimum_rate']}/hr")
print(f"  Recommended: ${s['recommended_rate']}/hr")
print(f"  Premium:     ${s['premium_rate']}/hr")
print(f"  Annual rev:  ${s['annual_revenue_at_recommended']:,.0f}")
