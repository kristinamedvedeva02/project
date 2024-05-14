


class Roles(object):
    COMPANY_ADMIN = 1
    OFFICE_ADMIN = 2
    TEAM_ADMIN = 3
    EMPLOYEE = 4

    ROLE_CHOICES = (
        (COMPANY_ADMIN, "Company admin"),
        (OFFICE_ADMIN, "Office admin"),
        (TEAM_ADMIN, "Team admin"),
        (EMPLOYEE, "Employee"),
    )