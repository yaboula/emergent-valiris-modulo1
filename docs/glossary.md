# Glossary

The ubiquitous language of Valiris Restaurants. Code, documentation and UI must use these terms consistently. The Spanish column is the canonical UI term.

**Layer** tells where the concept lives:
- **Platform:** sector-agnostic, reusable by future products.
- **Vertical:** specific to restaurants.
- **Module:** owned by one module.

## Organisation and access

| Term | Español (UI) | Layer | Definition |
| --- | --- | --- | --- |
| Tenant | Negocio | Platform | An isolated customer account of the platform. In this product, one tenant is one restaurant. All data carries a `tenant_id`. |
| Restaurant | Restaurante | Vertical | The restaurant-specific view of a tenant (cuisine, areas, tables, menu). |
| Member | Miembro del equipo | Platform | A person who can sign in to the owner panel of a tenant. |
| Role | Rol | Platform | The permission set of a member: `owner`, `manager` or `staff`. |
| Owner | Propietario | Platform | Role with full control, including billing and data deletion. |
| Manager | Encargado | Platform | Role that runs daily operations and configuration, without billing. |
| Staff | Personal de sala | Platform | Role for service tasks: seating, marking visits, scanning loyalty QR. |
| Feature flag | Módulo activo | Platform | Per-tenant switch that enables a module. |

## Guests and consent

| Term | Español (UI) | Layer | Definition |
| --- | --- | --- | --- |
| Customer | Cliente | Platform | A person known to a tenant (name, phone, email, language). Platform term. |
| Guest | Comensal | Vertical | A customer in the restaurant context. The UI says *comensal*; the code in the platform says `customer`. |
| Consent | Consentimiento | Platform | A recorded, revocable permission of a customer for a purpose and channel (e.g. marketing via WhatsApp), with timestamp and source. Required by GDPR/LSSI. |
| Channel | Canal | Platform | A communication medium: `email`, `whatsapp`, `sms`. |
| Visit | Visita | Platform | A record that a customer attended the business, created from a completed booking, a loyalty scan or manual entry. The central fact the review, loyalty and reactivation modules depend on. |
| Visit frequency | Frecuencia de visita | Module (reactivation) | The typical interval between a customer's visits, computed from their visit history. |
| Lapsed guest | Cliente en riesgo / inactivo | Module (reactivation) | A customer whose time since the last visit clearly exceeds their usual frequency. |

## Menu (storefront)

| Term | Español (UI) | Layer | Definition |
| --- | --- | --- | --- |
| Catalog | Catálogo | Platform | Generic list of offerable items of a tenant. In this product it is the menu. |
| Menu | Carta | Vertical | The restaurant's catalog, shown to guests. |
| Menu category | Sección de la carta | Vertical | A group of dishes (e.g. starters, mains, desserts). |
| Menu item / Dish | Plato | Vertical | A single item on the menu, with price, description, photo and allergens. |
| Variant | Variante | Platform | An alternative version of an item with its own price (e.g. half/full portion). |
| Modifier | Extra | Platform | An optional add-on to an item (e.g. extra cheese). |
| Allergen | Alérgeno | Vertical | One of the 14 allergens that must be declared under Regulation (EU) No 1169/2011, Annex II. |
| Daily offer | Oferta del día / Menú del día | Vertical | A time-limited item or set menu shown prominently. |
| Sold out | Agotado | Vertical | Temporary unavailability of an item, set in real time by staff. |
| Storefront | Escaparate / Web del restaurante | Module (storefront) | The public page of a restaurant: menu, hours, location, contact, booking entry point, highlights. |
| Table QR | QR de mesa | Module (storefront) | Printable QR code that opens the menu, optionally identifying the table. |

## Bookings

| Term | Español (UI) | Layer | Definition |
| --- | --- | --- | --- |
| Bookable resource | Recurso reservable | Platform | Anything with capacity and time that can be booked. In this product: a table. In future products: a chair, a room, a professional. |
| Table | Mesa | Vertical | A bookable resource with a minimum and maximum capacity, belonging to an area. |
| Area | Zona | Vertical | A part of the dining room (e.g. indoor, terrace) with its own tables and rules. |
| Service | Servicio | Vertical | A meal period with opening times (e.g. lunch, dinner). |
| Shift | Turno | Vertical | A seating window within a service (e.g. dinner first shift 20:00–22:00). |
| Slot | Franja horaria | Platform | A bookable start time offered to guests. |
| Party size | Número de comensales | Vertical | The number of people in a booking. |
| Cover | Cubierto | Vertical | One guest served. Used as the capacity and reporting unit. |
| Booking | Reserva | Module (booking) | A guest's claim on capacity for a date, time and party size. |
| Booking status | Estado de la reserva | Module (booking) | `pending`, `confirmed`, `seated`, `completed`, `cancelled`, `no_show`. |
| Walk-in | Sin reserva | Module (booking) | A guest seated without a prior booking. |
| Waitlist | Lista de espera | Module (booking) | Guests waiting for a slot or table to become available. |
| No-show | No presentado | Module (booking) | A confirmed booking whose guests did not arrive and did not cancel in time. |
| Deposit | Depósito / Señal | Module (booking) | An amount charged when booking, deducted from the bill or kept on no-show. |
| Card guarantee | Garantía con tarjeta | Module (booking) | A card saved (with Strong Customer Authentication) and charged only on no-show under the published policy. |

## Reviews, loyalty and messaging

| Term | Español (UI) | Layer | Definition |
| --- | --- | --- | --- |
| Review request | Solicitud de opinión | Module (reviews) | A message sent after a visit asking for feedback. |
| Private feedback | Opinión privada | Module (reviews) | Feedback received by the restaurant and not published. |
| Public review | Reseña pública | Module (reviews) | A review on a third-party platform (e.g. Google). |
| Review gating | Filtrado de reseñas | Module (reviews) | Asking only satisfied guests for public reviews. **Prohibited** by Google's policies; the product must not do it. |
| Loyalty program | Programa de fidelización | Module (loyalty) | The restaurant's rules for earning and redeeming rewards. |
| Stamp | Sello | Module (loyalty) | A unit earned per qualifying visit. |
| Reward | Recompensa | Module (loyalty) | A benefit redeemed after reaching a threshold. |
| Wallet pass | Tarjeta en Wallet | Module (loyalty) | A loyalty card stored in Apple Wallet or Google Wallet. |
| Reactivation campaign | Campaña de reactivación | Module (reactivation) | A consented message or offer sent to lapsed guests. |
| Conversation | Conversación | Module (whatsapp) | A WhatsApp thread between a guest and the restaurant. |
| Customer service window | Ventana de 24 h | Module (whatsapp) | WhatsApp rule: free-form replies are allowed within 24 h of the guest's last message; outside it, only approved templates. |
| Message template | Plantilla de mensaje | Platform | A pre-approved message with placeholders (required for WhatsApp outside the 24 h window). |
| Handover | Traspaso a humano | Module (whatsapp) | Switching a conversation from the assistant to a member of staff. |
| Notification | Notificación | Platform | Any outbound message, sent only through the platform notification service, which enforces consent and logs delivery. |

## Architecture

| Term | Definition |
| --- | --- |
| Platform | Sector-agnostic core and generic modules (`packages/platform/*`), reused by every Valiris product. |
| Vertical | Sector-specific domain logic (`packages/verticals/restaurants`). |
| App | A deployable product frontend (`apps/restaurants`). |
| Module | A bounded capability (storefront, booking, reviews, loyalty, reactivation, whatsapp) that depends on the core and never on another module. |
| Domain event | An immutable fact emitted by the core or a module (e.g. `visit.completed`), consumed by other modules. |
| RLS (Row Level Security) | PostgreSQL mechanism that restricts rows per tenant at the database level. |
