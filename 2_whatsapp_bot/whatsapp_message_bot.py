import random
import pywhatkit


def valid_phone_number(phone_number):
	""" 
	Check if user input is valid.
	Input is valid if the phone number begin with +972
	and 13 digits at length.
	"""
	if phone_number[:4] != "+972" or len(phone_number) != 13:
		print("Invalid input, try again")
		return False

	return True


def main():
	phone_number = input("Enter a phone number starting with +972: ")

	while valid_phone_number(phone_number) is False:
		phone_number = input("Enter a phone number starting with +972: ")

	print("\n")
	print("All times input should be in 24 time format without a minutes")
	# Time range for the script activity
	first_hour = int(input("Enter when do you want the script to begin: "))
	last_hour = int(input("Enter when do you want the script to finish: "))

	love_list = ["💜", "💖", "💓", "💞", "❤", "💕", "😻", "😍", "💘", "💓", "💗", "❣️", "😘", "💝", "💚", "💜", "💟"]

	while first_hour <= last_hour:

		# Chose a random number of emojis between 1-3
		emojis_quantity = random.randint(1, 3)
		min_generator = random.randint(12, 50)

		# Chose up to three random emojis from the love_list
		love_txt = " ".join(random.choices(love_list, k=emojis_quantity))

		# sendwhatmsg(phone_no: str, message: str, time_hour: int, time_min: int, wait_time: int = 20, tab_close: bool = False, close_time: int = 3) -> None
		# https://github.com/Ankit404butfound/PyWhatKit/wiki
		love_message = [phone_number, love_txt, first_hour, min_generator, 20, True, 3]

		pywhatkit.sendwhatmsg(*love_message)
		love_message[2] += 1

if __name__ == '__main__':
	main()