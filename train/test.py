# import numpy
# import matplotlib.pyplot as plt
# numpy.random.seed(2)

# x = numpy.random.normal(3, 1, 100)
# y = numpy.random.normal(150, 40, 100) / x


# print(x)
# plt.scatter(x, y)
# plt.show()

import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)
r2 = r2_score(train_y, mymodel(train_x))

print(mymodel(myline))

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()


# 1.
# Criminal Law - Criminal Lawyer Tel Aviv
# 5.0(1) · Attorney
# 10+ years in business · Tel Aviv-Yafo, Israel
# Open ⋅ Closes 12 AM · +972 3-673-8097


# 2.
# Rosenberg & Ovadia Law office
# 5.0(61) · Law firm
# Closed ⋅ Opens 8 AM Fri · +972 50-610-6180
# "Irena Rosenberg helped me obtaining and renewing my expert visa."


# 3.
# Its rays, divorce lawyer
# 5.0(23) · Divorce lawyer
# 15+ years in business · בני ברק, Israel
# Open 24 hours · +972 3-751-1105

# 4.
# David Zerbib avocat - דוד זרביב עורך דין
# 5.0(25) · Civil law attorney
# Tel Aviv-Yafo, Israel
# Closed ⋅ Opens 8:30 AM Sun · +972 54-445-8923

# 5.
# עו"ד גידי עזריה
# 5.0(10) · Attorney
# 3+ years in business · Be'er Sheva, Israel
# Closed ⋅ Opens 8 AM Sun · +972 8-669-9143
# Onsite services·
# Online appointments

# 6.
# עו״ד אילן בן ברוך
# 5.0(4) · Criminal justice attorney
# Be'er Sheva, Israel
# Open 24 hours · +972 50-626-3827

# 7.
# אילן אבירם חברת עורכי דין ושות'
# 5.0(27) · Law firm
# 20+ years in business · Be'er Sheva, Israel
# Closed ⋅ Opens 8:30 AM Sun · +972 8-623-5033


# 8.
# Aurelia KALFA Avocat francophone en Israël - אורליה כלפא עו'' ד - נדל"ן וירושה
# 5.0(9) · Attorney
# Ra'anana, Israel
# Closed ⋅ Opens 9 AM Sun · +972 54-680-4816


# 9.
# Law office in Tel Aviv | Lawyers in Tel Aviv - ZKGS
# No reviews · Attorney
# 10+ years in business · Tel Aviv-Yafo, Israel
# Open ⋅ Closes 7 AM Fri · +972 3-761-1611

# 10.
# Lior Ben Tzvi
# 5.0(1) · Family law attorney
# 5+ years in business · Netanya, Israel
# Closed ⋅ Opens 8 AM Fri · +972 53-973-9737

# 11.
# משרד עורכי דין טלוי קאופמן ושות'
# 5.0(2) · Attorney
# 5+ years in business · Tel Aviv-Yafo, Israel
# Closed ⋅ Opens 9 AM Sun · +972 3-691-6756


# 12.
# רומן סלזברג עורך דין Slezberg & Co. Law Office
# 5.0(21) · Law firm
# 5+ years in business · Tel Aviv-Yafo, Israel
# Closed ⋅ Opens 9 AM Sun · +972 54-342-2149
# Onsite services·
# Online appointments

# 13.
# Ministry lawyer Samuel Gorfein
# 5.0(2) · Attorney
# 7+ years in business · Bnei Brak, Israel
# Open ⋅ Closes 12 AM · +972 50-476-2428
# Onsite services·
# Online appointments


# 14.
# Richard Mann Law Offices South West Israel
# 5.0(3) · Attorney
# 5+ years in business · Ashkelon, Israel
# Closed ⋅ Opens 9 AM Sun · +972 54-481-1668

# 15.
# M.Hayman Wills and Enduring Powers of Attorney
# No reviews · Legal services
# Closed ⋅ Opens 8 AM Fri · +972 53-722-9212


# 16.
# Korakh & Co. Advocates & Patent Attorneys
# 4.0(4) · Patent attorney
# 7+ years in business · Tel Aviv-Yafo, Israel
# Closed ⋅ Opens 9 AM Sun · +972 3-644-9922


# 17.
# Victor Hlag life, lawyer
# 5.0(2) · Attorney
# 7+ years in business · Mevaseret Zion, Israel
# Closed ⋅ Opens 9 AM Sun · +972 54-226-2025
# Onsite services·
# Online appointments


# 18.
# The Aharoni Law Offices
# No reviews · Real estate attorney
# 5+ years in business
# Closed ⋅ Opens 9 AM Fri · +972 50-732-2688


# 19.
# Kovalenko & Co Law and Notary Office
# 4.4(20) · Legal services
# Tel Aviv-Yafo, Israel
# Closed ⋅ Opens 9 AM Sun · +972 54-680-2737

# 20.
# Yelnik Weiss & Co Law Firm
# No reviews · Attorney
# 10+ years in business · Tel Aviv-Yafo, Israel
# Closed ⋅ Opens 8 AM Sun · +972 3-691-1919


# 21.
# משרד עורכי דין - פוריאן אלמקייס
# 5.0(10) · General practice attorney
# Be'er Sheva, Israel
# Closed ⋅ Opens 8:30 AM Sun · +972 8-676-7501
# Onsite services·
# Online appointments


# 22.
# חיים הלוי עורך דין المحامي حاييم هاليڤي
# 4.9(55) · Attorney
# Be'er Sheva, Israel
# Closed ⋅ Opens 8 AM Sun · +972 53-499-1233


# 23.
# עורך דין אליהו אשר
# 5.0(28) · General practice attorney
# 5+ years in business · Dimona, Israel
# Closed ⋅ Opens 9 AM Sun · +972 50-777-6268
# Onsite services·
# Online appointments


# 24.
# גוונדשניידר גרימברג ראובן פירמת עורכי הדין לתעבורה
# 4.5(23) · Attorney
# 3+ years in business · Be'er Sheva, Israel
# Open 24 hours · +972 52-605-6613


# 25.
# Israeli Law Firm, Israeli Law, Law Firm Tel Aviv, Attorneys Israel
# No reviews · Family law attorney
# 10+ years in business · Israel
# +972 3-691-3999


# 26.
# Israeli Law Firm, Israeli Law, Law Firm Tel Aviv, Attorneys Israel
# No reviews · Family law attorney
# 10+ years in business · Israel
# +972 3-691-3999


# 27.
# Lior Ben Tzvi
# 5.0(1) · Family law attorney
# 5+ years in business · Netanya, Israel
# Closed ⋅ Opens 8 AM Fri · +972 53-973-9737



# 28.
# רומן סלזברג עורך דין Slezberg & Co. Law Office
# 5.0(21) · Law firm
# 5+ years in business · Tel Aviv-Yafo, Israel
# Closed ⋅ Opens 9 AM Sun · +972 54-342-2149
# Onsite services·
# Online appointments


# 29.
# Victor Hlag life, lawyer
# 5.0(2) · Attorney
# 7+ years in business · Mevaseret Zion, Israel
# Closed ⋅ Opens 9 AM Sun · +972 54-226-2025
# Onsite services·
# Online appointments


# 30.
# Yelnik Weiss & Co Law Firm
# No reviews · Attorney
# 10+ years in business · Tel Aviv-Yafo, Israel
# Closed ⋅ Opens 8 AM Sun · +972 3-691-1919


# 31.
# Kovalenko & Co Law and Notary Office
# 4.4(20) · Legal services
# Tel Aviv-Yafo, Israel
# Closed ⋅ Opens 9 AM Sun · +972 54-680-2737
# Online appointments


# 32.
# Korakh & Co. Advocates & Patent Attorneys
# 4.0(4) · Patent attorney
# 7+ years in business · Tel Aviv-Yafo, Israel
# Closed ⋅ Opens 9 AM Sun · +972 3-644-9922


# 33.
# Eli Gervits Law Office
# 1.0(1) · Attorney
# 5+ years in business · Tel Aviv-Yafo, Israel
# +972 3-758-5555


# 34.
# משרד עורכי דין טלוי קאופמן ושות'
# 5.0(2) · Attorney
# 5+ years in business · Tel Aviv-Yafo, Israel
# Closed ⋅ Opens 9 AM Sun · +972 3-691-6756

# 35.
# Portman Law Firm
# 5.0(1) · Law firm
# 7+ years in business · Jerusalem, Israel
# +972 2-563-0224


# 36.
# Richard Mann Law Offices South West Israel
# 5.0(3) · Attorney
# 5+ years in business · Ashkelon, Israel
# Closed ⋅ Opens 9 AM Sun · +972 54-481-1668


# 37.
# קוחלי-היקרי
# No reviews · General practice attorney
# Mevaseret Zion, Israel
# Closed ⋅ Opens 10 AM Sun · +972 2-561-9899


# 38.
# Lawyer Avigdor Joel
# 3.7(3) · Attorney
# 10+ years in business · Tel Aviv-Yafo, Israel
# Open ⋅ Closes 12 AM · +972 77-204-6773


# 39.
# Gilead Sher & Co. - Attorneys
# 5.0(2) · Attorney
# 10+ years in business · Tel Aviv-Yafo, Israel
# Closed ⋅ Opens 8:30 AM Sun · +972 3-601-5000


# 40.
# Ron Malul, a lawyer's office
# 5.0(1) · Attorney
# 7+ years in business · Herzliya, Israel
# Closed ⋅ Opens 9 AM Sun · +972 54-477-2820


# 41.

# Katri Gabriel, lawyer
# 4.5(20) · Attorney
# 10+ years in business · Herzliya, Israel
# Closed ⋅ Opens 9:30 AM Sun · +972 9-950-9504


# 42.
# Rotenstein & Levy Law Firm
# 5.0(2) · Law firm
# 7+ years in business · Netanya, Israel
# Closed ⋅ Opens 9 AM Sun · +972 9-773-2880


# 43.
# Israel Law Team
# No reviews · Attorney
# 5+ years in business · Jerusalem, Israel
# +972 52-353-0042

# 44.
# Murlakov Law Office
# No reviews · Attorney
# 7+ years in business · Tel Aviv-Yafo, Israel
# Closed ⋅ Opens 9 AM Sun · +972 52-836-0503
# Onsite services·
# Online appointments

# 45.
# Eyal Frost Law Office & Notary
# No reviews · Attorney
# 10+ years in business · Tel Aviv-Yafo, Israel
# Closed ⋅ Opens 9 AM Sun · +972 3-561-3399


# 46.
# At Lawyers
# No reviews · Attorney
# 5+ years in business · Tel Aviv-Yafo, Israel
# +972 77-201-3690


# 47.
# Lawyer Ty Assad
# No reviews · Attorney
# 7+ years in business · Sajur, Israel
# Closed ⋅ Opens 8 AM Sun · +972 52-787-0006

# 48.
# Jacob Rosenberg, attorney and notary
# 4.9(13) · Attorney
# 10+ years in business · Bnei Brak, Israel
# Closed ⋅ Opens 10 AM Sun · +972 3-578-3383
# Onsite services·
# Online appointments


# 49.
# Israel Bar Association, Haifa Districts
# 4.5(58) · General practice attorney
# 10+ years in business · Haifa, Israel
# +972 4-853-7079


# 50.
# Adir Lapid, Attorney
# 5.0(3) · Attorney
# 30+ years in business · Herzliya, Israel
# Closed ⋅ Opens 9 AM Sun · +972 52-250-7061


# 51.
# Moti Levi. criminal lawyer
# 5.0(7) · Attorney
# 10+ years in business · Tel Aviv-Yafo, Israel
# +972 3-691-1433

# 52.
# Sandrine Moyal Lawyer עו״ד סונדרין מויאל
# No reviews · Attorney
# 7+ years in business · Ramat Gan, Israel
# Closed ⋅ Opens 10 AM Fri · +972 54-613-9733


# 53.
# Saar Alon, IP Attorney | סער אלון, עו"ד, קניין רוחני
# No reviews · Attorney
# Closed ⋅ Opens 8 AM Sun · +972 54-699-5669
# Online appointments


# 54.
# Hacohen
# No reviews · Attorney
# 5+ years in business · Jerusalem, Israel
# +972 2-622-2335


# 55.
# UK Immigration and Visas Israel
# 5.0(7) · Immigration attorney
# 10+ years in business · Herzliya, Israel
# Closed ⋅ Opens 8 AM Fri · +972 3-737-0070



# 56.
# Nivin Asali, Law Firm
# No reviews · Civil law attorney
# Closed ⋅ Opens 8 AM Sat · +972 50-886-6484


# 57.
# AVOCAT FRANCOPHONE EN ISRAEL
# No reviews · Real estate attorney
# 7+ years in business · Lod, Israel
# Closed ⋅ Opens 8:30 AM Fri · +972 50-694-8007

# 58.
# NA Law Firm
# No reviews · Attorney
# 3+ years in business
# +972 4-851-6518



# 59.
# Snow Abraham, Lawyer
# 5.0(2) · Family law attorney
# 10+ years in business
# Closed ⋅ Opens 9 AM Fri · +972 50-666-6667


# 60.
# Lawyer Reuven Chaikin - Environmental and Safety Law, Licensing Business
# No reviews · Attorney
# 3+ years in business · Tel Aviv-Yafo, Israel
# Closed ⋅ Opens 9 AM Sun · +972 50-488-7868


# 61.
# Zarabi & Co. Law Firm
# No reviews · Law firm
# 3+ years in business · Tel Aviv-Yafo, Israel
# Closed ⋅ Opens 9 AM Sun · +972 54-303-0283


# 62.
# Eddie Lazar - lawyers
# 5.0(4) · Attorney
# 10+ years in business · Ramat Hasharon, Israel
# +972 3-547-3443


# 63.ליכט פטרן ושות' משרד עורכי דין
# No reviews · Attorney
# 5+ years in business · Tel Aviv-Yafo, Israel
# +972 3-974-4920


# 64.
# Doron Bar-El, Notary and lawyers company
# 1.0(1) · Attorney
# 10+ years in business · Petah Tikva, Israel
# Closed ⋅ Opens 8:30 AM Sun · +972 3-913-3334






