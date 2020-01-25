#
# Conditional build:
%bcond_with	tests		# perform "make test" (requires Internet connection)
#
%define	pdir	WWW
%define	pnam	Google-Groups
Summary:	WWW::Google::Groups - Google Groups Agent
Summary(pl.UTF-8):	WWW::Google::Groups - czytnik Google Groups
Name:		perl-WWW-Google-Groups
Version:	0.09
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	14e9991909162ace95c70723294c2f8b
URL:		http://search.cpan.org/dist/WWW-Google-Groups/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Date::Parse) >= 2.24
BuildRequires:	perl-Email-Simple >= 1:1.6
BuildRequires:	perl-TimeDate >= 1:1.14
BuildRequires:	perl-WWW-Mechanize >= 0.5
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW::Google::Groups - Google Groups Agent.

%description -l pl.UTF-8
WWW::Google::Groups - czytnik Google Groups.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	< /dev/null
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/WWW/Google/*.pm
%{perl_vendorlib}/WWW/Google/Groups
%{_mandir}/man3/*
