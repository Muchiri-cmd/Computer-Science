Imports System.Data.SqlTypes

Public Class Form1
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        lstMenu.Items.Add("1.Ugali Matumbo ")
        lstMenu.Items.Add("2. Karanga Chapo ")
        lstMenu.Items.Add("3.Muthokoi Nyama ")
        lstMenu.Items.Add("4.Githeri Plain ")
        lstMenu.Items.Add("5. Wet mix Fries ")
        lstMenu.Items.Add("6. Water ")

    End Sub

    Private Sub btnAgizaMlo_Click(sender As Object, e As EventArgs) Handles btnAgizaMlo.Click
        Dim ChaguoLako As Integer
        Dim orders As Integer
        Dim order As Integer
        Dim Bill As Decimal = 0.00

        orders = InputBox("How many orders are you placing ? ")

        For order = 1 To orders

            ChaguoLako = InputBox("Enter Item No to place order ")

            Dim UgaliMatumboPrice As Decimal = (180.0)
            Dim KarangaChapoPrice As Decimal = (150.0)
            Dim MuthokoiNyamapPrice As Decimal = (170.0)
            Dim GitheriPlainPrice As Decimal = (100.0)
            Dim WetMixFriesPrice As Decimal = (250.0)
            Dim umquantity As Integer
            Dim kcquantity As Integer
            Dim mnquantity As Integer
            Dim gpquantity As Integer
            Dim wfquantity As Integer

            Select Case (ChaguoLako)

                Case 1
                    umquantity = InputBox("Enter quantity ")

                    MessageBox.Show("You ordered for " & umquantity & " Ugali Matumbo Price pay is ksh " & UgaliMatumboPrice * umquantity)
                Case 2
                    kcquantity = InputBox("Enter quantity ")

                    MessageBox.Show("You ordered for " & kcquantity & " Karanga Chapo.Price pay is: " & KarangaChapoPrice * kcquantity)
                Case 3
                    mnquantity = InputBox("Enter quantity ")

                    MessageBox.Show("You ordered for " & mnquantity & " Muthokoi Nyama. Price pay is: " & MuthokoiNyamapPrice * mnquantity)
                Case 4
                    gpquantity = InputBox("Enter quantity ")

                    MessageBox.Show("You ordered for " & gpquantity & " Githeri Plain .Price pay is: " & GitheriPlainPrice * gpquantity)
                Case 5
                    wfquantity = InputBox("Enter quantity ")

                    MessageBox.Show("You ordered for " & wfquantity & " wet mix fries. Price pay is: " & WetMixFriesPrice * wfquantity)
                Case Else
                    MessageBox.Show("You took plain Water only.You'll pay NOTHING ")
            End Select
            Bill = Bill + UgaliMatumboPrice * umquantity + KarangaChapoPrice * kcquantity + MuthokoiNyamapPrice * mnquantity +
                GitheriPlainPrice * gpquantity + WetMixFriesPrice * wfquantity

        Next order

        MessageBox.Show("Your total bill is " & Bill)
        MessageBox.Show("FUKUZA NJAA KIOSK " & vbCrLf &
                        "Thank You for Dining With us " & vbCrLf &
                        "COME AGAIN ")

    End Sub


End Class
