#!/usr/bin/env python3

class Person:
    
    def get_name(self):
        return self._name

    def set_name(self, name):
        if (name == "" or type(name) in (int, float) or len(name) > 25 or len(name) <= 1 ):
            print("Name must be string between 1 and 25 characters.")
        else: 
            self._name = name.title()


    def get_job(self):
        return self._job

    def set_job(self, job):
        approved_jobs = ["Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal", "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"]

        if job in approved_jobs:
            self._job = job
        else: 
            print("Job must be in list of approved jobs.")
        


    name = property(get_name, set_name)
    job = property(get_job, set_job)