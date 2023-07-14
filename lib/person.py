#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self,name="Tong",job = "Sales"):
        self.name = name
        self.job = job

    def get_name(self):
        return self._name
    
    def get_job(self):
        return self._job
    
    def set_name(self,name):
        if(isinstance(name, str) and (0 < len(name) < 25)):
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    def set_job(self,job):
        if(isinstance(job, str)) and job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")
    
    name = property(get_name, set_name)
    job = property(get_job, set_job)