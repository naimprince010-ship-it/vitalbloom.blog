import { revalidatePath, revalidateTag } from "next/cache";
import { NextRequest, NextResponse } from "next/server";

type RevalidateRequestBody = {
  path?: string;
  tag?: string;
};

export async function POST(request: NextRequest) {
  const secret = request.nextUrl.searchParams.get("secret");

  if (!process.env.CMS_PREVIEW_SECRET || secret !== process.env.CMS_PREVIEW_SECRET) {
    return NextResponse.json({ message: "Invalid revalidation secret." }, { status: 401 });
  }

  let body: RevalidateRequestBody = {};

  try {
    body = (await request.json()) as RevalidateRequestBody;
  } catch {
    body = {};
  }

  const path = body.path || "/";

  revalidatePath(path);

  if (body.tag) {
    revalidateTag(body.tag, "max");
  }

  return NextResponse.json({
    revalidated: true,
    path,
    tag: body.tag ?? null,
    timestamp: new Date().toISOString()
  });
}
