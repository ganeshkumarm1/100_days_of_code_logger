import os
from datetime import datetime
from string import Template

log_folder = "D:/GaNeShKuMaRm/GiThUb/100-days-of-code"
log_file = log_folder + "/log.md"

def get_log_details():
	log_details = {}
	log_details['date'] = datetime.now().strftime("%d, %B %Y (%A)")
	print "Today's Date: " + log_details['date']
	log_details['day'] = raw_input('Day: ')
	log_details['progress'] = raw_input("Today's Progress: ")
	total_links = input('Number of links to be added: ')
	links = []
	for l in range(total_links):
		link_text = raw_input('Text: ')
		link_url = raw_input('Url: ')
		links.append({'text': link_text, 'url': link_url})
	log_details['links'] = links
	return log_details

def preview(log_details):
	print "Today's Date: " + log_details['date']
	print "Day: " + log_details['day']
	print "Today's Progress: " + log_details['progress']
	print "Links\n-----"
	for link in log_details['links']:
		print link['text'] + ": " + link['url']

def separator(length):
	print ''.join(['-'] * length)

def get_log_markdown(log_details):
	markdown_template = ''
	day_template = Template("### Day $day: $date\n\n")
	progress_template = Template("**Today's Progress**: $progress\n\n")
	links_template = Template("$i. [$text]($url)\n")
	log_md = day_template.substitute(day=log_details['day'], date=log_details['date']) + progress_template.substitute(progress=log_details['progress']) + "**Link(s) to work**\n"
	i = 1
	for l in log_details['links']:
		log_md += links_template.substitute(i=i, text=l['text'], url=l['url'])
		i += 1
	return log_md + '\n\n'

def write_log_to_file(file_name, content):
	with open(file_name, 'a') as file_handle:
		file_handle.write(content)

def push_to_repo(commit_message):
	os.chdir(log_folder)
	os.system("git add log.md")
	os.system("git commit -m \"" + commit_message + "\"")
	os.system("git push origin master")

def main():
	log_details = get_log_details()
	separator(100)
	preview(log_details)
	separator(100)
	push_to_git = raw_input("Do you want to push the changes to git (y/n): ")
	if push_to_git == 'y' or push_to_git == 'Y':
		new_log = get_log_markdown(log_details)
		write_log_to_file(log_file, new_log)
		push_to_repo("Day " + log_details['day'] + " - " + log_details['date'])
		print "Pushed log to repo :)"

if __name__ == "__main__":
    main()