Public Class Form1
    Private Sub btnNumbers_Click(sender As Object, e As EventArgs) Handles btnNumbers.Click
        Dim i As Integer
        Dim numZum As Integer
        Dim jina As String
        jina = InputBox("Enter ur name plz", "KARIBU", "Nameless")
        lstNames.Items.Clear()
        numZum = 0
        For i = 2 To 20 Step 2
            lstNames.Items.Add(i)
            numZum = numZum + i

        Next i
        lstNames.Items.Add(" Their sum is " & numZum)


        For i = 1 To 20
            If (i Mod 2 = 0) Then
                lstNames.Items.Add(i)
                numZum = numZum + i
            End If
        Next i
        lstNames.Items.Add("Their sum is " & numZum)

        For i = 1 To 20 Step 1
            If (i Mod 3 = 0 Or i Mod 6 = 0) Then
                lstNames.Items.Add(i)
                numZum = numZum + i
            End If
        Next i
        lstNames.Items.Add("Their sum is " & numZum)


        For i = 1 To 20 Step 1
            If (i Mod 3 = 0 And i Mod 6 = 0) Then
                lstNames.Items.Add(i)
                numZum = numZum + i
            End If
        Next i
        lstNames.Items.Add("Their sum is " & numZum)

        For i = 1 To 20 Step 1
            If (i Mod 3 = 0 Xor i Mod 6 = 0) Then
                lstNames.Items.Add(i)
                numZum = numZum + i
            End If
        Next i
        lstNames.Items.Add("Their sum is " & numZum)
    End Sub

    Private Sub btnExit_Click(sender As Object, e As EventArgs) Handles btnExit.Click
        Dim response As Integer
        response = MessageBox.Show("Are you sure you want to exit ", "Funga Program ", MessageBoxButtons.RetryCancel,
                                 MessageBoxIcon.Warning)
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim output As String
        For index As Integer = 1 To 5
            output = output & index & vbNewLine
        Next
        MessageBox.Show(output)
    End Sub
End Class
