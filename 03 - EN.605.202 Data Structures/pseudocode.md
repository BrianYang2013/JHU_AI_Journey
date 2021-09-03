# zyBooks

## Module 1 - Complexity and ADTs

### Top five by array

Figure 1.6.1: Algorithm to determine the top five salespersons using an array.

```
DisplayTopFiveSalespersons(allSalespersons) {
   // topSales array has 5 elements
   // Array elements have subitems for name and total sales
   // Array will be sorted from highest total sales to lowest total sales
   topSales = Create array with 5 elements 
   
   // Initialize all array elements with a negative sales total
   for (i = 0; i < topSales⇢length; ++i) {
      topSales[i]⇢name = ""
      topSales[i]⇢salesTotal = -1
   }

   for each salesPerson in allSalespersons {
      // If salesPerson's total sales is greater than the last
      // topSales element, salesPerson is one of the top five so far
      if (salesPerson⇢salesTotal > topSales[topSales⇢length - 1]⇢salesTotal) {

         // Assign the last element in topSales with the current salesperson
         topSales[topSales⇢length - 1]⇢name =  salesPerson⇢name 
         topSales[topSales⇢length - 1]⇢salesTotal =  salesPerson⇢salesTotal 

         // Sort topSales in descending order	=> *** Move smallest to topSales[topSales⇢length - 1] ***
         SortDescending(topSales)
      }
   }

   // Display the top five salespersons
   for (i = 0; i < topSales⇢length; ++i) {
      Display topSales[i] 
   }
}
```