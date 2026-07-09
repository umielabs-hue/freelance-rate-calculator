"""Consultant Profile Example"""
import sys; sys.path.insert(0, "..")
from models import FreelanceProfile

p = FreelanceProfile(
    desired_monthly_income=10000,
    monthly_business_expenses=1200,
    tax_rate=0.30,
    benefits_overhead=0.15,
    weekly_work_hours=40,
    utilization_rate=0.50,  # Consultants spend more on business dev
    weeks_per_year=44,
    buffer_multiplier=1.3,
)
s = p.summary()
print("Management Consultant Rates")
print(f"  Minimum:     ${s['minimum_rate']}/hr")
print(f"  Recommended: ${s['recommended_rate']}/hr")
print(f"  Premium:     ${s['premium_rate']}/hr")
print(f"  Annual rev:  ${s['annual_revenue_at_recommended']:,.0f}")
