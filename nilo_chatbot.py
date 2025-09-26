{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8338e353-da46-4532-89ee-010c97139481",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Nilo(user_input):\n",
    "    user_input = user_input.lower()\n",
    "    if \"hello\" in user_input or \"hi\" in user_input:\n",
    "        return \"Hey there! How can I help you today?\"\n",
    "    elif \"how are you\" in user_input:\n",
    "        return \"I'm just a bunch of code, but I'm feeling pretty smart today!\"\n",
    "    elif \"basketball\" in user_input:\n",
    "        return (\"Basketball is a sport that is commonly played by 2 teams \"\n",
    "                \"with five players each aiming to make as many baskets as possible.\")\n",
    "    elif \"bye\" in user_input:\n",
    "        return \"Catch you later, Clive!\"\n",
    "    else:\n",
    "        return \"Hmm... I’m not sure how to respond to that yet.\"\n",
    "\n",
    "# Chat loop\n",
    "while True:\n",
    "    user_input = input(\"You: \")\n",
    "    if user_input.lower() == \"exit\":\n",
    "        print(\"Nilo: Goodbye!\")\n",
    "        break\n",
    "    response = Nilo(user_input)\n",
    "    print(\"Nilo:\", response)\n"
   ]
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
   "version": "3.12.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
