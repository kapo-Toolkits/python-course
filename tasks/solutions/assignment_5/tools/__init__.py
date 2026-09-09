"""tools — დამხმარე ფუნქციების პაკეტი.

ეს ფაილი აღნიშნავს, რომ საქაღალდე პაკეტია. შეიძლება სულ ცარიელი იყოს,
მაგრამ აქ მას „ფასადად“ ვიყენებთ: ორივე მოდულს ერთად შემოგვაქვს, რომ
`from tools import mathtools, textutils` მუშაობდეს ერთი ხაზით.
"""

from . import mathtools, textutils

__all__ = ["mathtools", "textutils"]
