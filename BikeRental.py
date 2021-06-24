# ----------------------------------------------------------------------------------------------------------------------------------
# Assignment Name:      Bicycle Shop
# Name:                 Neina Cichon
# Date:                 2020-07-26
# ----------------------------------------------------------------------------------------------------------------------------------

#Declare Global Variables
rentHourly = 5.00
rentDaily = 20.00
rentWeekly = 60.00
discount = .3
bikeStock = 20

class Rental:
   
    def __init__(self, rentalQty, rentalType):
        self.rentalQty = rentalQty
        self.rentalType = rentalType
    
    #Get Rental type and Display Amount
    def calcRental(self):
        global bikeStock
        if self.rentalQty <= 0:
            raise Exception('Bike rental quantity must be greater than zero. You entered: {}'.format(self.rentalQty))
        elif self.rentalQty > bikeStock:
            print("We currently only have ", bikeStock, "bikes in stock.")
        else:
            if self.rentalType == 'hourly':
                bikeStock -= self.rentalQty
                global rentHourly
                global rentAmount
                rentAmount = rentHourly            
                return rentAmount
                #Get Day/Time of Rental
     
            elif self.rentalType == "daily":
                bikeStock -= self.rentalQty
                global rentDaily
                rentAmount = rentDaily
                #Get Day/Time of Rental
           
            elif self.rentalType == "weekly":
                bikeStock -= self.rentalQty
                global rentWeekly
                rentAmount = rentWeekly
                return rentAmount
                #Get Day/Time of Rental
                
            else:
                 raise Exception('Rental Type was not "hourly", "daily", or "weekly". You entered: {}'.format(self.rentalType)) 
            return rentalType
            
class Return:
  
    def __init__(self, rentalQty, rentalType, rentalTime):
        self.rentalQty = rentalQty
        self.rentalType = rentalType
        self.rentalTime = rentalTime

        global bikeStock
        bikeStock += rentalQty
    
    #Process Return, add returned bikes to inventory, and display amount due
    def calcReturn(self):
        if self.rentalType == "daily":
            global rentDaily
            #Get Day/Time of Return
            rentalAmount = (rentDaily * rentalTime) * rentalQty
        elif self.rentalType == "weekly":
            global rentWeekly
            #Get Day/Time of Return
            rentalAmount = (rentweekly * rentalTime) * rentalQty
        else:
            global rentHourly
            #Get Day/Time of Return
            rentalAmount = (rentHourly * rentalTime) * rentalQty

        if rentalQty >= 3 and rentalQty <= 5:
            print("Family Discount: $", (rentalAmount * discount))
            amountDue = rentalAmount * (rentalAmount * discount)
            return amountDue
        else:
            amountDue = rentalAmount
            return amountDue
        print("Amount Due: $", amountDue)


#-----------------------------------------------------

Rental1 = Rental(1, 'daily')
Rental2 = Rental(10, 'hourly')
Return1 = Return(1, "daily", 2)
#Return2 = Return(1, 2)

print( 'Qty of bikes in stock: ', (bikeStock))
#print("Renting", str(Rental.calcRental(rentalQty)), "bikes." "\nYou will be charged $", str(Rental.calcRental(rentAmount)), str(Rental(rentalType)), "for each bike.")
#print("Renting", Rental.calcRental(rentalQty), "bikes." "\nYou will be charged $",  "per week for each bike.")