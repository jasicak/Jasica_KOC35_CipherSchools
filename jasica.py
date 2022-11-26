{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "78845268",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Date of Birth18\n",
      "Enter Month of Birth 7\n",
      "Enter Year of Birth 2003\n",
      "Enter Todays Date 26\n",
      "Enter Present Month 11\n",
      "Enter Present Year 2022\n",
      "('You have survived', 7071, 'Days')\n"
     ]
    }
   ],
   "source": [
    "dd1=int(input(\"Enter Date of Birth\"))      #Taking Inputs from the user\n",
    "mm1=int(input(\"Enter Month of Birth \"))\n",
    "yyyy1=int(input(\"Enter Year of Birth \"))\n",
    "dd2=int(input(\"Enter Todays Date \"))\n",
    "mm2=int(input(\"Enter Present Month \"))\n",
    "yyyy2=int(input(\"Enter Present Year \"))\n",
    "\n",
    "\n",
    "#Intializing an array with the number of days in all the 12 months\n",
    "monthDays = [31, 28, 31, 30, 31, 30,     \n",
    "             31, 31, 30, 31, 30, 31]\n",
    "\n",
    "\n",
    "#Defining a function to count the number of leap years \n",
    "def countleapyears(x,y):\n",
    "\n",
    "    if x<=2:\n",
    "        y-=1\n",
    "    #A leap year should be a multiple of 4 and 400 but should not be a multiple of 100\n",
    "    #so the below formula is used to calculate the number of leap years\n",
    "    return int(y / 4) - int(y / 100) + int(y / 400)\n",
    "\n",
    "\n",
    "#Defining a function to calculate the number of days till the given date\n",
    "def getn(a,b,c):\n",
    "    #Multiplying the Number of years with 365 and adding the number of days in the current month\n",
    "    n1=c*365+a\n",
    "\n",
    "    #Using a for loop to add the days of all the previous months in the given year\n",
    "    for i in range(0,b-1):\n",
    "        n1 += monthDays[i]\n",
    "   \n",
    "   #Adding the Number of Leapdays by calling the countLeapyear function\n",
    "    n1+=countleapyears(b,c)\n",
    "    \n",
    "    #Returns the number of days passed till the given date\n",
    "    return(n1)\n",
    "#Finding the number of days passed till the date of birth\n",
    "a=getn(dd1,mm1,yyyy1)\n",
    "\n",
    "#Finding the number of days passed till the Peresent date\n",
    "b=getn(dd2,mm2,yyyy2)\n",
    "\n",
    "#The total number of days survived is the difference between a and b\n",
    "ans=(\"You have survived\",b-a,\"Days\")\n",
    "print(ans)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "06379247",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
