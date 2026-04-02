# Appendices

[← Back to TOC](./TOC.md)

---

## Appendix A: Next.js CLI Quick Reference

```bash
# Create new project
npx create-next-app@latest my-app
npx create-next-app@latest my-app --typescript --tailwind --app

# Development server (hot reload)
npm run dev

# Production build
npm run build

# Start production server (after build)
npm start

# Run linter
npm run lint
```

### Project Structure (App Router)

```text
my-app/
├── app/                    # App Router root
│   ├── layout.tsx          # Root layout (wraps all pages)
│   ├── page.tsx            # Home page (/)
│   ├── globals.css
│   ├── about/
│   │   └── page.tsx        # /about route
│   ├── blog/
│   │   ├── page.tsx        # /blog route
│   │   └── [slug]/
│   │       └── page.tsx    # /blog/my-post (dynamic route)
│   └── api/
│       └── users/
│           └── route.ts    # /api/users API route
├── components/             # Reusable React components
├── lib/                    # Utilities, data fetching helpers
├── public/                 # Static assets (images, fonts)
└── next.config.js          # Next.js configuration
```

---

## Appendix B: Core Concepts Reference

### Rendering Strategies

| Strategy | How | When to Use |
|----------|-----|-------------|
| **SSR** (Server-Side Rendering) | Page rendered on server per request | Data changes frequently; needs to be fresh |
| **SSG** (Static Site Generation) | Page rendered at build time | Content rarely changes (blog posts, docs) |
| **ISR** (Incremental Static Regeneration) | Static, but regenerates on a schedule | Mix of performance and freshness |
| **CSR** (Client-Side Rendering) | Page rendered in browser | Interactive dashboards, user-specific data |

### Server Components vs Client Components

```tsx
// Server Component (default) — runs only on the server
// Can: access databases, read files, use async/await directly
// Cannot: use hooks, handle events, use browser APIs

// app/users/page.tsx
async function UsersPage() {
  const users = await db.getUsers();  // direct DB access!
  return (
    <ul>
      {users.map(u => <li key={u.id}>{u.name}</li>)}
    </ul>
  );
}

export default UsersPage;
```

```tsx
// Client Component — "use client" directive at the top
// Can: use useState, useEffect, onClick, browser APIs
// Cannot: be async, access server-side resources directly

'use client';
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  return (
    <button onClick={() => setCount(c => c + 1)}>
      Count: {count}
    </button>
  );
}

export default Counter;
```

### App Router — File Conventions

```text
app/
  layout.tsx        — Wraps children; persists across navigation
  page.tsx          — The page component for a route segment
  loading.tsx       — Shown while page is loading (Suspense boundary)
  error.tsx         — Error UI for this route (must be 'use client')
  not-found.tsx     — Shown when notFound() is called
  template.tsx      — Like layout but re-mounts on navigation
  route.ts          — API route handler (GET, POST, etc.)
```

### Dynamic Routes

```tsx
// app/blog/[slug]/page.tsx — matches /blog/hello-world

interface Props {
  params: { slug: string };
}

export default async function BlogPost({ params }: Props) {
  const post = await getPost(params.slug);
  return <article>{post.content}</article>;
}

// Generate static paths for SSG
export async function generateStaticParams() {
  const posts = await getAllPosts();
  return posts.map(post => ({ slug: post.slug }));
}
```

### API Routes (Route Handlers)

```ts
// app/api/users/route.ts

import { NextRequest, NextResponse } from 'next/server';

// GET /api/users
export async function GET(request: NextRequest) {
  const users = await db.getUsers();
  return NextResponse.json(users);
}

// POST /api/users
export async function POST(request: NextRequest) {
  const body = await request.json();
  const user = await db.createUser(body);
  return NextResponse.json(user, { status: 201 });
}
```

---

## Appendix C: Data Fetching Patterns

### fetch with Caching

```tsx
// Server Component — data fetching with cache control

// Cache indefinitely (SSG behavior)
const data = await fetch('https://api.example.com/data', {
  cache: 'force-cache',
});

// No cache (SSR behavior — fresh on every request)
const data = await fetch('https://api.example.com/data', {
  cache: 'no-store',
});

// Revalidate every 60 seconds (ISR behavior)
const data = await fetch('https://api.example.com/data', {
  next: { revalidate: 60 },
});
```

### Server Actions (Form Submissions)

```tsx
// app/contact/page.tsx
// Server Actions let you handle form POST directly in a Server Component

async function submitContact(formData: FormData) {
  'use server';  // This function runs on the server
  const email = formData.get('email') as string;
  const message = formData.get('message') as string;
  await db.saveMessage({ email, message });
}

export default function ContactPage() {
  return (
    <form action={submitContact}>
      <input name="email" type="email" required />
      <textarea name="message" required />
      <button type="submit">Send</button>
    </form>
  );
}
```

---

## Appendix D: next.config.js Reference

```js
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Image optimization — allow external domains
  images: {
    domains: ['images.unsplash.com', 'cdn.mysite.com'],
  },

  // URL rewrites — rewrite /api/v1/users → external API
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'https://backend.mysite.com/api/:path*',
      },
    ];
  },

  // Redirects
  async redirects() {
    return [
      {
        source: '/old-blog/:slug',
        destination: '/blog/:slug',
        permanent: true,   // 308 redirect (SEO-safe)
      },
    ];
  },

  // Environment variables exposed to the browser
  // (prefix with NEXT_PUBLIC_ in .env files instead)
  env: {
    CUSTOM_KEY: process.env.CUSTOM_KEY,
  },
};

module.exports = nextConfig;
```

---

## Appendix E: Performance Checklist

| Area | Technique |
|------|-----------|
| Images | Use `<Image>` from `next/image` (automatic WebP, lazy loading, sizing) |
| Fonts | Use `next/font` to self-host fonts (avoids layout shift) |
| Components | Use Server Components by default; only use `'use client'` when needed |
| Data | Use `cache: 'force-cache'` for static data; `no-store` only when truly needed |
| Bundle | Avoid importing entire libraries (`lodash` → `lodash/get`) |
| Suspense | Wrap slow components in `<Suspense>` with `loading.tsx` |
| Dynamic imports | Use `next/dynamic` to code-split large client components |

```tsx
// Dynamic import — load heavy component only when needed
import dynamic from 'next/dynamic';

const HeavyChart = dynamic(() => import('@/components/Chart'), {
  loading: () => <p>Loading chart...</p>,
  ssr: false,   // disable server rendering (for browser-only libs)
});
```

---

## Appendix F: Glossary

**App Router**
The newer Next.js routing system (introduced in Next.js 13). Routes are defined by folder structure in `app/`, and supports React Server Components, Layouts, and Server Actions.

**Pages Router**
The original Next.js routing system. Routes are files in `pages/`. Still supported but App Router is recommended for new projects.

**Server Component**
A React component that renders only on the server. Can fetch data, access databases, and read environment variables directly. No JavaScript is sent to the client for this component.

**Client Component**
A React component with the `'use client'` directive. Runs in the browser and supports hooks, event handlers, and browser APIs.

**Hydration**
The process of attaching React's event handlers to server-rendered HTML. After the browser receives the HTML, React "hydrates" it — making it interactive.

**ISR (Incremental Static Regeneration)**
A rendering strategy where static pages are regenerated in the background after a time interval without requiring a full rebuild. Combines the performance of static pages with the freshness of server rendering.

**Middleware**
A Next.js `middleware.ts` file at the project root that runs on every request before it reaches a route. Used for authentication, redirects, A/B testing, and internationalization.

**Server Action**
A function marked with `'use server'` that runs on the server, callable from client components or forms. Replaces the need for separate API routes for form submissions and mutations.

---

## Appendix G: Resources

- [Next.js Docs](https://nextjs.org/docs) — official documentation
- [Next.js Examples](https://github.com/vercel/next.js/tree/canary/examples) — official example projects
- [Vercel Deployment Guide](https://vercel.com/docs/frameworks/nextjs) — deploy to Vercel
- [Next.js Learn](https://nextjs.org/learn) — official interactive tutorial
