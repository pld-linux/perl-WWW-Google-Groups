#
# Conditional build:
%bcond_with	tests		# perform "make test" (requires Internet connection)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	WWW
%define	pnam	Google-Groups
Summary:	WWW::Google::Groups - Google Groups Agent
#Summary(pl):	
Name:		perl-WWW-Google-Groups
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/WWW/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	14e9991909162ace95c70723294c2f8b
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Date::Parse) >= 2.24
BuildRequires:	perl(Email::Simple) >= 1.6
BuildRequires:	perl(WWW::Mechanize) >= 0.5
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW::Google::Groups - Google Groups Agent.

# %description -l pl
# TODO

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
