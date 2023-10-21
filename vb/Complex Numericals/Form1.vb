Public Class Form1
    Private Sub btnCost_Click(sender As Object, e As EventArgs) Handles btnCost.Click
        Dim decPrice As Decimal
        Dim iQuantity As Integer
        Dim decTotalCost As Decimal
        Dim decDiscount As Decimal
        Dim decPostage As Decimal
        'BO(DM)(AS)
        'PE(MD)(AS)
        decPrice = 5
        iQuantity = 10
        decDiscount = 2
        decPostage = 3
        decTotalCost = (decPrice - decDiscount) * iQuantity + decPostage
        MessageBox.Show("Total cost is : " & decTotalCost & " kshs")
    End Sub
End Class
