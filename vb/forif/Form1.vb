Public Class Form1
    Private Sub btneven_Click(sender As Object, e As EventArgs) Handles btneven.Click
        Dim iMax As Integer
        Dim stOddorEven As String
        Dim x As Integer
        iMax = InputBox("what number do you count to? ")
        stOddorEven = InputBox("Do you want odd numbers or even numbers?")
        stOddorEven = stOddorEven.ToLower

        If stOddorEven = "even" Then
            For x = 2 To iMax Step 2
                MsgBox(x)
            Next
        ElseIf stOddorEven = "odd" Then
            For x = 1 To iMax Step 2
                MsgBox(x)

            Next
        End If
    End Sub
End Class
