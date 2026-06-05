#!/usr/bin/python3
"""
Module for generating personalized invitation files from a template and attendee list.
"""
import os
import logging

def generate_invitations(template, attendees):
    """
    Generate invitation files from a template and a list of attendees.

    Args:
        template (str): The invitation template containing placeholders.
        attendees (list of dict): List of dictionaries with attendee data.

    Returns:
        None
    """
    # Input type validation
    if not isinstance(template, str):
        logging.error("Invalid input: template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        logging.error("Invalid input: attendees must be a list of dictionaries.")
        return

    # Empty input checks
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with values from attendee dict, defaulting to "N/A"
        output = template
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(placeholder, "N/A")
            if value is None:
                value = "N/A"
            output = output.replace("{" + placeholder + "}", str(value))

        # Write to output file
        filename = f"output_{index}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(output)

        # Log success (optional, not required by spec)
        print(f"Generated {filename}")

if __name__ == "__main__":
    # Example usage (will not run when imported)
    pass
