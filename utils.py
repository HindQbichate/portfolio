def all_tags(projects):
    tags = set()
    for project in projects:
        for tag in project["tags"]:
            tags.add(tag)
    return sorted(tags)

def filter_projects(projects, chosen):
    if len(chosen) == 0:
        return projects
    result = []
    for project in projects:
        for tag in project["tags"]:
            if tag in chosen:
                result.append(project)
                break
    return result