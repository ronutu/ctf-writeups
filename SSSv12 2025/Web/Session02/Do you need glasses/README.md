# Do you need glasses?

## Description

Get the flag from [glasses](http://141.85.224.70:8086/).

## Intuition

We look in the source code.

## Solution

In the source code there is a Base64 encoded password: `<meta content="anVreG9xbm5jYQ==" name="password">`. This translates to `jukxoqnnca`.

In the source code we also see a `staff.html` page commented and we visit that page. It is a login page. Looking in the source code there is a checkbox commented so we uncomment it and check it and then enter the credentials from before.

This leads to a `admin.php` page which has in the source code this shifted flag `MMM{1_ly4ffs_f1ey_f34p1ha_nl4w3m_1h_w0gg3hnm}`. We rotate it and find the flag.

## Flag

`SSS{1_re4lly_l1ke_l34v1ng_tr4c3s_1n_c0mm3nts}`
