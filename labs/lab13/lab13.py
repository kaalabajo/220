"""
Name: Kaala Bajo
lab13.py

Problem: Sends alerts at specified trading volumes

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
def trade_alert(filename):
    #open the file, read it, put the contents in a list
    in_f = open(filename, "r")
    all_trades = in_f.read()
    trades_list = all_trades.split(" ")

    #take the list, make all the entries numbers
    for index in range(len(trades_list)):
        trades_list[index] = eval(trades_list[index])

    #cool now run it
    for i in range(len(trades_list)):
        if trades_list[i] >= 830:
            print("WARNING: trading volume exceeded 830 at {} (actual: {:1})".format( (i+1),(trades_list[i])  ))

        elif trades_list[i] == 500:
            print("ALERT: trading volume hit 500 at {}".format(i+1))

    in_f.close()

def main():
    trade_alert("trades.txt")