"""
Core calculation models.
"""
from dataclasses import dataclass

@dataclass
class FreelanceProfile:
    desired_monthly_income: float
    monthly_business_expenses: float
    tax_rate: float
    benefits_overhead: float = 0.15
    weekly_work_hours: float = 40.0
    utilization_rate: float = 0.65
    weeks_per_year: float = 48.0
    buffer_multiplier: float = 1.2

    @property
    def monthly_billable_hours(self):
        return round((self.weekly_work_hours * self.utilization_rate * self.weeks_per_year) / 12, 1)

    @property
    def monthly_gross_needed(self):
        net = self.desired_monthly_income + self.monthly_business_expenses
        gross = net / (1 - self.tax_rate - self.benefits_overhead)
        return round(gross * self.buffer_multiplier, 2)

    @property
    def minimum_rate(self):
        return round(self.monthly_gross_needed / self.monthly_billable_hours, 2)

    @property
    def recommended_rate(self):
        return round(self.minimum_rate * 1.5, 2)

    @property
    def premium_rate(self):
        return round(self.minimum_rate * 2.5, 2)

    @property
    def annual_revenue(self):
        return round(self.recommended_rate * self.monthly_billable_hours * 12, 2)

    def summary(self):
        return {
            "monthly_billable_hours": self.monthly_billable_hours,
            "monthly_gross_needed": self.monthly_gross_needed,
            "minimum_rate": self.minimum_rate,
            "recommended_rate": self.recommended_rate,
            "premium_rate": self.premium_rate,
            "annual_revenue_at_recommended": self.annual_revenue,
        }
