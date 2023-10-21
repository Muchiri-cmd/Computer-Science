Public Class Form1
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub

    Private Sub btnWeekdays_Click(sender As Object, e As EventArgs) Handles btnWeekdays.Click
        Dim SikuLeo As Integer
        SikuLeo = InputBox("Enter an integer in the values 1 to 7 ")

        If (SikuLeo = 5) Then
            MessageBox.Show("Leo ni FURAHI DAY.Member's Day ")
        ElseIf (SikuLeo = 3) Then
            MessageBox.Show("Today is WEDNESDAY ")
        ElseIf (SikuLeo = 7) Then
            MessageBox.Show("Leo ni Sunday. Praise and glory to the almighty ")
        Else
            MessageBox.Show("Longing for FRIDAY ")
        End If
        MessageBox.Show("Life continues ")
    End Sub

End Class
